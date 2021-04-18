import turtle
import pandas

screen = turtle.Screen()
screen.title("Juego de las Provincias Argentinas")
image = "argentina_sin.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("prov_arg.csv")
provincias = data["Provincia"].to_list()

answer_state = screen.textinput(title="Provincias Argentinas", prompt="Nombrá una Provincia")
# TODO: Convert the guess to Title case
answer_title = answer_state.title()

# TODO: Check if the guess is among the 24 provinces
for name in provincias:
    if answer_title == provincias[name]:


# TODO: El bardo acá es que tengo que armar una clase aparte para la tortuga que escribe las provincias.



#
# TODO: Write correct guesses onto the map
# TODO: USe a loop to allow the user to keep guessing
# TODO: Record the correct guesses in a list
# TODO: Keep track of the score



# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

screen.exitonclick()