from graphics import *
def main():

    win = GraphWin("Face", 750,750)

    center = Point(750/2,750/2)
    circ = Circle(center,300)
    circ.setFill('gold')
    circ.draw(win)

    center = Point(750/2,500)
    circ = Circle(center,100)
    circ.setFill('black')
    circ.draw(win)

    input("Press any key to quit")

main()

