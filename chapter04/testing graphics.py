from graphics import *
def main():

    win = GraphWin("My Circle")
    center = Point(100,100)
    circ = Circle(center,30)
    circ.setFill('red')
    circ.draw(win)

    win.getMouse()

main()
