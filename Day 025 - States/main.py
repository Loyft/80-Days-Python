import turtle
import pandas

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

screen = turtle.Screen()
screen.title("US Stats Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States", prompt="Whats another State's name?")
    cap_answer = answer_state.capitalize()

    if cap_answer == "Exit":
        break

    if cap_answer in all_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == cap_answer]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(cap_answer)
        guessed_states.append(cap_answer)

states_to_learn = []

for state in data.state:
    if state not in guessed_states:
        states_to_learn.append(state)

df = pandas.DataFrame(states_to_learn)
df.to_csv("states_learn.csv")

screen.exitonclick()
