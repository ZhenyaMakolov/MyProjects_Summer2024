from turtle import *
from random import *

speed(0)
hideturtle()
Screen().bgcolor('black')
Screen().colormode(255)


def move(x, y):
    '''перемещение в точку экрана по координатам'''
    penup(), goto(x, y), pendown()


def star(x, y):
    '''звезда произвольного цвета, размера и количества сторон'''
    move(x, y)
    elements_stars = choice([3, 4, 5, 6, 7, 8, 10, 12, 15, 17, 20])
    corner_element = 180 / elements_stars
    length_star = randint(5, 50)
    new_color = (randrange(0, 255), randrange(0, 255), randrange(0, 255))
    fillcolor(new_color), pencolor(new_color), begin_fill()
    left(randint(1, 360))
    if elements_stars == 3:
        for _ in range(elements_stars):
            forward(length_star), right(170), forward(length_star), left(50)
    else:
        for _ in range(elements_stars):
            forward(length_star), right(180 - corner_element * 3), forward(length_star), left(180 - corner_element)
    end_fill()


def left_mouse_click(x, y):
    '''считывание координат места клика мыши по экрану'''
    star(x, y)
    

Screen().onclick(left_mouse_click)
Screen().listen()
w = Screen()
w.mainloop()