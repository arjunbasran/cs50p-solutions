import pytest
from project import bulk_bw_frac_per_week, cut_bw_frac_per_week, show_bulking_kcal, show_cutting_kcal, show_targets_table, get_met_total


def test_bulk_bw_frac_per_week():
    assert bulk_bw_frac_per_week(0.1) == pytest.approx(0.051667*0.1 - 0.033333*(0.1**2))
    assert bulk_bw_frac_per_week(0.15) == pytest.approx(0.051667*0.15 - 0.033333*(0.15**2))


@pytest.mark.parametrize("p", [0.05, 0.1, 0.2])
def test_cut_bw_frac_per_week_positive_and_monotonic(p):
    val = cut_bw_frac_per_week(p)
    assert val > 0


def test_difference_between_cut_bw_frac_per_week():
    assert cut_bw_frac_per_week(0.2) > cut_bw_frac_per_week(0.05)


def test_show_bulking_kcal_and_kg():
    tdee = 2700
    weight = 80
    data = show_bulking_kcal_and_kg(tdee, weight)

    expected_keys = ["mild", "moderate", "fast"]
    assert list(data.keys()) == expected_keys

    for values in data.values():
        assert values.keys() == {"kcal", "kg"}
        assert len(values["kcal"]) == 2
        assert len(values["kg"]) == 2

    kcal_low, kcal_high = data["mild"]["kcal"]
    assert kcal_low < kcal_high
    assert kcal_low == pytest.approx(tdee * (1 + 0.05))


def test_show_cutting_kcal_and_kg():
    tdee = 2700
    weight = 80
    data = show_cutting_kcal_and_kg(tdee, weight)

    expected_keys = ["mild", "moderate", "fast"]
    assert list(data.keys()) == expected_keys

    for values in data.values():
        assert values.keys() == {"kcal", "kg"}
        assert len(values["kcal"]) == 2
        assert len(values["kg"]) == 2

    kcal_low, kcal_high = data["mild"]["kcal"]
    assert kcal_low < kcal_high
    assert kcal_low == pytest.approx(tdee * (1 - 0.15))


def test_show_targets_table_prints_col_names_and_title(capsys):
    bulking = {"mild":{"kcal":(3334,3493),"kg":(0.2,0.39)},
               "moderate":{"kcal":(3493,3651),"kg":(0.39,0.56)},
               "fast":{"kcal":(3651,3810),"kg":(0.56,0.72)}}
    cutting = {"mild":{"kcal":(2699,2858),"kg":(0.39,0.56)},
               "moderate":{"kcal":(2540,2699),"kg":(0.56,0.72)},
               "fast":{"kcal":(2223,2540),"kg":(0.72,1)}}

    show_targets_table(bulking, cutting)
    out = capsys.readouterr().out

    assert "Calorie Wizard" in out
    assert "Phase" in out
    assert "Calories/day" in out
    assert "kg/week" in out
    assert "Outcome" in out












