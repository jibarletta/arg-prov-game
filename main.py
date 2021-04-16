import turtle

screen = turtle.Screen()
screen.title("Juego de las Provincias Argentinas")
image = "argentina_sin.gif"
screen.addshape(image)
turtle.shape(image)

answer_state = screen.textinput(title="Adiviná la Provincia", prompt="¿Cuál es el nomrbe de otra provincia?")
print(answer_state)

# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

screen.exitonclick()