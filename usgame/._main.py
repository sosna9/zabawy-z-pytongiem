import turtle
import pandas

screen = turtle.Screen()
screen.title("zgaduj stany")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

dupa = pandas.read_csv("50_states.csv")
all_states = dupa.state.to_list()
guessed_states = []


while len(guessed_states)<50:
    answer_state = screen.textinput(title="Dupa", prompt="daj no").title()


    if (answer_state in all_states):
        guessed_states.append(answer_state)
        print("HURRA")
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = dupa[dupa.state == answer_state]
        print(state_data)
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())

    else:
        print("Chuj")

screen.exitonclick()
