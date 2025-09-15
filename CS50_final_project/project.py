"""
CS50P Final Project - Calorie Calculator

Takes in user info (sex, age, height, weight), works out BMR (for estimate) or TDEE (for exact 24h energy expenditure),
then shows bulking + cutting targets with kcal/day and estimated weekly BW change. User can get an estimate or an exact
value depending on what they type. Output is shown in Rich tables for easier reading.
"""

from rich.console import Console
from rich.table import Table
from difflib import get_close_matches
import re

ACTIVITIES = {
            "sleep": 0.9, "sit": 1.3, "walk": 3, "run": 10.0, "cycle": 8.0, "weightlift": 6.0,
            "football": 8.0, "basketball": 7.0, "tennis": 7.0, "swim": 8.0, "yoga": 3.0, "dance": 4.5,
            "hike": 6.0, "gardening": 4.0, "clean": 3.5, "cook": 2.5, "study": 1.3, "office": 1.3
            }

TIME_REGEX = re.compile(r"\b(\d+(?:\.\d+)?)\s*(h|hr|hrs|hour|hours|min|mins|minute|minutes)\b")

BULKING_RANGES = {
    "mild": (0.05, 0.1),
    "moderate": (0.1, 0.15),
    "fast": (0.15, 0.2)
}

CUTTING_RANGES = {
    "mild": (0.1, 0.15),
    "moderate": (0.15, 0.2),
    "fast": (0.2, 0.3)
}

# For the BW change models below: y is fraction of BW/week, p is daily % change vs TDEE (e.g., p=0.10 for +10%).
# Using a quadratic y = a*p - b*p^2 so it tapers at higher surpluses/deficits.
# Anchors are chosen from evidence-based ranges for trained lifters.
# Rule of thumb: ~7700 kcal ≈ 1 kg. So Δkcal/day -> kg/week via (Δkcal*7)/7700.

def bulk_bw_frac_per_week(p):
    """
    Weekly bulking BW gain fraction for a surplus p (p = fraction of TDEE).
    Anchors I’m using (rounded):
      p=0.10 (+10%) -> y=0.0048  (0.48% BW/wk)
      p=0.20 (+20%) -> y=0.0090  (0.90% BW/wk)
    Solve:
      0.0048 = 0.1a - 0.01b
      0.0090 = 0.2a - 0.04b -> a=0.051, b=0.030
    Final:
      y = 0.051*p - 0.030*p**2
    """
    return 0.051*p - 0.030*(p**2)

def cut_bw_frac_per_week(p):
    """
    Weekly cutting BW loss fraction for a deficit p (p = fraction of TDEE).
    Anchors I’m using (rounded):
      p=0.20 (−20%) -> y=0.0090  (0.90% BW/wk)
      p=0.30 (−30%) -> y=0.0120  (1.20% BW/wk)
    Solve:
      0.0090 = 0.2a - 0.04b
      0.0120 = 0.3a - 0.09b  -> a=0.055, b=0.050
    Final:
      y = 0.055*p - 0.050*p**2
    """
    return 0.055*p - 0.050*(p**2)


def show_targets_table(bulking_dict, cutting_dict):
    """
    Prints bulking + cutting targets side by side in a Rich table.
    """

    table = Table(title="Calorie Wizard", show_lines = True)
    table.add_column("Phase", style="cyan", justify="center")
    table.add_column("Calories/day", style="cyan", justify="center")
    table.add_column("kg/week (estimate)", style="cyan", justify="center")
    table.add_column("Outcome (for trained individuals)", style="cyan", justify="center")

    outcomes_bulk = {
        "mild": "Slow muscle gain, minimal fat gain",
        "moderate": "Good muscle growth, some fat gain",
        "fast": "Max muscle already hit, extra = fat"
    }

    for phase, vals in bulking_dict.items():
        kcal_low, kcal_high = vals["kcal"]
        kg_low, kg_high = vals["kg"]
        table.add_row(
            f"{phase.capitalize()} Bulk",
            f"{kcal_low:.0f}–{kcal_high:.0f} kcal",
            f"{kg_low:.2f}–{kg_high:.2f} kg GAINED per week",
            outcomes_bulk[phase]
        )

    table.add_row("","","","")

    outcomes_cut = {
        "mild": "Slow fat loss, muscle mostly preserved",
        "moderate": "Faster fat loss, some muscle loss",
        "fast": "Rapid fat loss, high muscle loss risk"
    }

    for phase, vals in cutting_dict.items():
        kcal_low, kcal_high = vals["kcal"]
        kg_low, kg_high = vals["kg"]
        table.add_row(
            f"{phase.capitalize()} Cut",
            f"{kcal_low:.0f}–{kcal_high:.0f} kcal",
            f"{kg_low:.2f}–{kg_high:.2f} kg LOST per week",
            outcomes_cut[phase]
        )

    console = Console()
    console.print(table)

def show_bulking_kcal_and_kg(tdee, weight):
    """
    Returns kcal and kg/wk ranges for mild, moderate, and fast bulks.
    Uses the keys and values in the global dictionary 'BULKING_RANGES'
    """

    results = {}
    for label, (low, high) in BULKING_RANGES.items():
        kcal_low  = tdee * (1 + low)
        kcal_high = tdee * (1 + high)
        kg_low  = weight * bulk_bw_frac_per_week(low)
        kg_high = weight * bulk_bw_frac_per_week(high)

        results[label] = {
            "kcal": (kcal_low, kcal_high),
            "kg": (kg_low, kg_high)
        }
    return results

def show_cutting_kcal_and_kg(tdee, weight):
    """
    Returns kcal and kg/wk ranges for mild, moderate, and fast cuts.
    Uses the keys and values in the global dictionary 'CUTTING_RANGES'
    """

    results = {}
    for label, (low, high) in CUTTING_RANGES.items():
        kcal_low  = tdee * (1 - high)
        kcal_high = tdee * (1 - low)
        kg_low  = weight * bulk_bw_frac_per_week(low)
        kg_high = weight * bulk_bw_frac_per_week(high)

        results[label] = {
            "kcal": (kcal_low, kcal_high),
            "kg": (kg_low, kg_high)
        }
    return results

def get_met_total():
    """
    User inputs an activity and its duration, until total duartion = 24h.
    Uses regex to parse durations and difflib to fuzzy-match activity names.
    Returns total MET-hours which is equal to (Σ MET(activity) * hours).
    """

    total_hours = 0
    sum_met_hours = 0
    options = ",\n".join(ACTIVITIES.keys())
    remaining = 24
    print(f"\n\nEnter an activity and how long you do it for every day on average\n\nThese are the options: \n\n{options} \n\n(you must enter a total of 24h)")
    activity_hours = {}

    while True:
        sentence = input("\n>>> ").lower().strip()
        match = TIME_REGEX.search(sentence)
        if not match:
            print("\nCouldn't find anything like '2h' or '90 mins'")
            continue

        time = float(match.group(1))
        unit = match.group(2)
        if unit.startswith("h"):
            hours = time
        else:
            hours = round(time / 60, 1)

        words = re.findall(r"[a-z]+", sentence)
        activity = None
        matches = []

        for word in words:
            closest = get_close_matches(word, ACTIVITIES.keys(), n=3, cutoff=0.7)
            if len(closest) == 1:
                matches.append(closest[0])
            elif len(closest) > 1:
                print("\nPlease be more specific.")
                continue

        if len(set(matches)) == 0:
            print(f"\nCouldn't detect an activity. Options are:\n\n{options}")
            continue
        elif len(set(matches)) > 1:
            print(f"\nOnly enter one activity at a time. Detected: {', '.join(set(matches))}")
            continue
        else:
            activity = matches[0]


        proposed_hours = dict(activity_hours)           # copy dict so I can "test" adding this actvity (prevents corrupting the real dict if invalid)
        proposed_hours[activity] = hours
        total_hours = sum(proposed_hours.values())      # gets a value for total_hours before if statement

        if total_hours > 24:
            print(f"\nThat would make {total_hours}h in total (more than 24h). You have {remaining} hours left")
            continue

        activity_hours[activity] = hours                # only adds activity and hours if valid

        print("\nSO FAR:")
        for act, hrs in activity_hours.items():
            print(f"- {act.capitalize():<12}: {hrs:.1f}h")

        remaining = 24 - total_hours
        if remaining <= 0:
            print("\ngreat, day complete!")
            break
        else:
            print(f"\nplease enter what you do in the remaining {remaining:.1f} hours")

    sum_met_hours = sum(ACTIVITIES[a] * h for a, h in activity_hours.items())
    return sum_met_hours

def bmr(weight, height, age, sex):
    """
    Returns Basal Metabolic Rate using Mifflin–St Jeor forumla.
    Male: 10W + 6.25H − 5A + 5; Female: 10W + 6.25H − 5A − 161.
    """

    if sex.lower() == "male" or "m":
        return (10 * weight + 6.25 * height - 5 * age + 5)
    elif sex.lower() == "female" or "f":
        return float(10 * weight + 6.25 * height - 5 * age - 161)

class Data:
    """
    Collect & validate user inputs (sex, age, height, weight).
    Keeps related attributes together for cleaner passing between functions.
    """

    def __init__(self):
        self.sex = self.ask_sex()
        self.age = self.ask_age()
        self.height = self.ask_height()
        self.weight = self.ask_weight()

    def ask_sex(self):
        while True:
            s = input("\nEnter your sex (m/f): ").strip().lower()
            if s in ("male", "m", "female", "f"):
                return s
            print("Please type male/m or female/f.")

    def ask_age(self):
        while True:
            try:
                age = int(input("\nEnter your age (must be between 18-65): "))
                if not 18 <= age <= 65:
                    print("age must be a whole number between 18 and 65")
                    continue
                return age
            except ValueError:
                print("please enter a valid age (must be a whole number between 18 and 65)")
                continue

    def ask_height(self):
        while True:
            try:
                height = int(input("\nEnter your height in cm (only enter an integer): "))
                if not 120 <= height <= 250:
                    print("please enter a valid number (120cm - 250cm)")
                    continue
                return height
            except ValueError:
                print("please only enter an ineteger for your height (120cm - 250cm)")
                continue

    def ask_weight(self):
        while True:
            try:
                weight = int(input("\nEnter your weight in kilograms (only enter an integer): ").strip())
                if not 30 <= weight <= 300:
                    print("please enter a valid weight (30kg - 300kg)")
                    continue
                return weight
            except ValueError:
                print("please only enter an integer for your weight value (30kg - 300kg)")
                continue


def main():
    user = Data()
    user.sex
    user.age
    user.height
    user.weight
    calculated_bmr = bmr(user.weight, user.height, user.age, user.sex)

    while True:
        question = input("\nWould you like an exact value, which requires more Qs, or a rough estimate (enter 'exact' or 'estimate')? ").lower().strip()
        if question not in ('exact', 'estimate'):
            print("please enter either 'exact' or 'estimate'")
            continue

        elif question == "exact":

            sum_met_hours = get_met_total()
            tdee = float(1.05 * user.weight * sum_met_hours)                  # Multiply by 1.05 to roughly account for digestion (TEF) and small errors in the 1 MET = 1 kcal/kg/hr assumption


            bulking_dict = show_bulking_kcal_and_kg(tdee, user.weight)
            cutting_dict = show_cutting_kcal_and_kg(tdee, user.weight)

            show_targets_table(bulking_dict, cutting_dict)

        else:

            PAL = ["sedentary", "light", "moderate", "intense", "very intense"]
            info = (
                ">>> Sedentary:         desk/student life, little planned exercise. Steps/day = <5k\n"
                ">>> Light:             some daily movement or light exercise 1–3×/week. Steps/day = ~5-7.5k\n"
                ">>> Moderate:          exercise 3–5×/week or on-feet job. Steps/day = ~7.5-10k\n"
                ">>> Intense:           hard training most days and/or physically demanding job. Steps/day = ~10-14k\n"
                ">>> Very Intense:      heavy manual labor + intense training; athletes in season. Steps/day = >14k\n"
            )

            while True:
                activity_multiplier = input(f"\nEnter a physical activity level (choose 'sedentary', 'light', 'moderate', 'intense' or 'very intense') given the info below:\n\n{info}\n\n").lower().strip()
                if activity_multiplier not in PAL:
                    print("\nplease enter one of the choices")
                    continue

                elif activity_multiplier == "sedentary":
                    tdee = calculated_bmr * 1.2
                    break

                elif activity_multiplier == "light":
                    tdee = calculated_bmr * 1.375
                    break

                elif activity_multiplier == "moderate":
                    tdee = calculated_bmr * 1.55
                    break

                elif activity_multiplier == "intense":
                    tdee = calculated_bmr * 1.725
                    break

                else:
                    tdee = calculated_bmr * 1.9
                    break

            bulking_dict = show_bulking_kcal_and_kg(tdee, user.weight)
            cutting_dict = show_cutting_kcal_and_kg(tdee, user.weight)

            show_targets_table(bulking_dict, cutting_dict)

        break

    protein_bulk_low = round(user.weight * 1.6)
    protein_bulk_high = round(user.weight * 2.2)
    protein_cut_low = round(user.weight * 2)
    protein_cut_high = round(user.weight * 2.6)


    print("\n----------------------------------------------PROTEIN INTAKE----------------------------------------------\n\n"
        f"Finally, for muscle growth, protein intake is crucial. You should be aiming for around {protein_bulk_low}g - {protein_bulk_high}g protein\n"
        f"when bulking, and around {protein_cut_low}g - {protein_cut_high}g protein when cutting, in order to preserve muscle\n\n"
    )

if __name__ == "__main__":
    main()



