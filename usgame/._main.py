import turtle
import pandas

screen = turtle.Screen()
screen.title("zgaduj stany")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

dupa = pandas.read_csv("50_states.csv")
all_states = dupa.state.to_list()
dfstate = pandas.read_csv("stany zgadniete")
guessed_states = []
x = dfstate.Stan.values.tolist()
guessed_states += x
print(guessed_states)

for state in guessed_states:
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    state_data = dupa[dupa.state == state]
    print(state_data)
    t.goto(int(state_data.x), int(state_data.y))
    t.write(state_data.state.item())


while len(guessed_states)<50:
    answer_state = screen.textinput(title="Dupa", prompt="daj no").title()

    if answer_state == "Exit" :break
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
print(guessed_states)
df = pandas.DataFrame(guessed_states, columns=["Stan"])
df.to_csv("stany zgadniete")
screen.exitonclick()
