import turtle
import pandas
from turtles import Scoreboard

screen = turtle.Screen()
screen.title("Juego de las Provincias Argentinas")
image = "argentina_sin.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("prov_arg.csv")
provincias = data["Provincia"].to_list()
x_coord = data['x'].to_list()
y_coord = data['y'].to_list()
score = Scoreboard()
score.update_score()
nombre_prov = Scoreboard()
correct_guesses = []

# Use a loop to allow the user to keep guessing
game_is_on = True

while game_is_on:
    # Convert the guess to Title case
    answer_state = screen.textinput(title="Provincias Argentinas", prompt="Nombrá una Provincia")
    answer_title = answer_state.title()

    # Check if the guess is among the 24 provinces
    for name in provincias:
        if answer_title == name and answer_title not in correct_guesses:
            # Write correct guesses onto the map
            nombre_prov.write_province(provi=name, xcoord=int(x_coord[provincias.index(name)]),
                                       ycoord=int(y_coord[provincias.index(name)]))
            # Record the correct guesses in a list
            correct_guesses.append(answer_title)
            # Keep track of the score
            score.point()
            if len(correct_guesses) == 25:
                score.you_win()
                game_is_on = False

screen.exitonclick()
