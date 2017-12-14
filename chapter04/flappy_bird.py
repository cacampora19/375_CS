#falppy_bird.py

from  graphics import *

def main():

    print("Press the right arrow key to start and the up arrow key to move.")

    window_size = 900
    canvas_size = 36

    lose = False

    delta_y = canvas_size/2

    win = GraphWin("Flappy Bird", window_size, window_size)
    win.setCoords(0, 0, canvas_size, canvas_size)
    win.setBackground("light sky blue")

    message_text = Text(Point(canvas_size/2, canvas_size/2), "Click to start")
    message_text.setTextColor("red")
    message_text.setFace("courier")
    message_text.setSize(30)
    message_text.setStyle("bold")
    message_text.draw(win)
    win.getMouse()
    message_text.setText("")

    bird = Circle(Point(canvas_size/2, delta_y), 3)
    bird.setFill("yellow")
    bird.setOutline("yellow")
    bird.draw(win)

    while lose == False:
        key = win.checkKey()

        delta_x = 0
        delta_y = 0

        if key == "Up":
            delta_y = delta_y + 5

        bird.move(delta_x, delta_y)


main()
