# File: chaos.py
# A simple program illustrating chaotic behavior

def main():
    print("This program illustrates a chaotic function")
    loopNumber = eval(input("How many times would you like to loop?: "))
    x = eval(input("Enter a number between 0 and 1: "))
    for i in range(loopNumber):
        x = 3.9 * x * (1 - x)
        print(i + 1, "-", x)

    print("Done")

main()
