import pandas
import turtle

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

#reads csv and stores as DataFrame
states_data = pandas.read_csv("50_states.csv")
state_names = states_data["state"].tolist()


correct_guesses = []


# TODO : 4. Use a loop to allow the user to keep guessing
while len(correct_guesses) < 50:
    # TODO : 1. Convert the guess to Title case
    # TODO : 6. Keep track of the score
    answer_state = screen.textinput(title=f"{len(correct_guesses)}/50 Correct", prompt="What's another state's name?").title()
    # TODO : 2. Check if the guess is among the 50 states
    if answer_state in state_names:
        # TODO : 3. Write correct guesses onto the map
        state_row = states_data[states_data.state == answer_state]
        x = int(state_row.x)
        y = int(state_row.y)
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        t.goto(x,y)
        t.write(answer_state)
        # TODO : 5. Record the correct guesses in a list
        correct_guesses.append(answer_state)
        print(correct_guesses)

    elif answer_state=='Exit':
        # TODO : at end of game, create csv with just the states missed out
        for item in correct_guesses:
            state_names.remove(item)
        new_dataframe = pandas.DataFrame(state_names)
        new_dataframe.to_csv("states_to_learn.csv")
        break

screen.exitonclick()
