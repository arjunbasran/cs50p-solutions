# CALORIE WIZARD - CS50P Final Project

#### Video Demo:  <https://youtu.be/dLt96q8e7hI>
#### Description:
Calorie Wizard is my CS50P Final Project. It’s a Python program that works out your daily calorie needs for whether you want to gain weight or lose weight. You enter your details such as age, sex, height, and weight and the program calculates either your **BMR** (a quick baseline estimate) or your **total MET-hours** (a more precise value for daily expenditure based on what you do in a day) depending on whether you want an approximate or more precise value for your TDEE. Once a TDEE value is calculated, some further calculations are carried out and a table is produced using the `rich` library, showing **bulking** (calorie surplus) and **cutting** (calorie deficit) kcal targets at ranges mild, moderate, and fast. It also contains estimates for **weekly bodyweight change** (using a quadratic formula that takes the fractional surplus/deficit and turns it into a projected weekly gain or loss based on observed scientific data), as well as a short sentence describing the **outcome** from consuming X amount of kcal.

---

## Files in this project
- `project.py` – the main program with all the logic and user interaction.
- `requirements.txt` – the libraries I imported (just `rich` and `pytest`).
- `test_project.py` – the unit tests I wrote to check calculations and dict.

---

## Design Choices
- I gave users the option to choose between a quick **estimate** (BMR) and a more detailed **exact** calculation (TDEE). This way the program works for both casual users and those who want accuracy.
- I used **global dictionaries** to store the calorie ranges for bulking and cutting. This kept the values in one place instead of scattering them through functions, which made the code easier to manage.
- For activity input, I used **regex** so the program could accept flexible formats like `2h`, `2 hours`, or `120 mins`. This was important for me because I wanted users to be able to type full sentences in a loop, like `i walk for 90 mins` or `i study for 3 hours`, instead of having two separate prompts for activity and time. It feels more natural this way and less like filling out a survey.
- I chose the `rich` library for output so I could display the results in neat tables instead of plain text.
- I used a quadratic formula to estimate weekly bodyweight change, instead of the standard “divide (surplus/deficit) calories by 7” rule. The simple linear method assumes weight gain scales perfectly with surplus (e.g. a 3000 kcal surplus would cause exactly 3× the weight gain of a 1000 kcal surplus). In reality, the body becomes less efficient at converting huge surpluses or deficits into weight changes. The quadratic approach curves the results, so large surpluses/deficits scale more realistically and give better estimates.

---

## What I Learned
- **Regex:** At first it was confusing, but I learned how to parse messy user inputs properly, and saw how much more powerful and efficient it is for input validation compared to simpler methods like conditionals and loops
- **Libraries:** Using external libraries like `rich` showed me how to pull in tools to improve my program beyond the basics.
- **Code placement:** I learned the hard way that where code goes really matters. In my `get_met_total()` function, I kept running into bugs and weird behaviour just because I declared things in the wrong place - like putting a variable before an if validation, or forgetting to move something outside the while True loop. The program would either break or give unexpected results. Once I got the order and scope right, everything clicked.
- **Testing:** Writing `test_project.py` gave me a glimpse of the power of pytest. I learned how to use features like `capsys` to capture and check printed output, and `@pytest.mark.parametrize` to quickly test multiple inputs without writing separate test functions. This showed me how much easier and more efficient testing can be with pytest compared to manually checking results.
- **Reading documentation:** I learned how to read documentation properly. Building a program this long meant I needed lots of functions and methods, some that I’d seen before and some completely new. I had to dig into the docs for things like `get_close_matches`, or even simple methods like `.join`, to really understand how and why they work. That forced me to slow down, learn the details, and apply them correctly instead of just copying code from examples and hoping it worked.




