import turtle
import pandas

correct_choices = []
score = 0

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

#creating a while loop until you get all states
while len(correct_choices) < 50:
    answer_state = screen.textinput(title=f"{len(correct_choices)}/50 States Correct",
                                    prompt="What's State's name").title()
    if answer_state == "Exit":
        #using list comprehensions.
       missing_states = [state for state in all_states if state not in correct_choices]
       #creating a csv with missing states by you
       new_data = pandas.DataFrame(missing_states)
       new_data.to_csv("States_to_learn.csv")
       break
    #if answer is correct it will write it in the spot of the state
    if answer_state in all_states:
        correct_choices.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

