import math

def main():

    print("This program solves the pythagorean theorem with 1 unknown")
    unknownVariable = input("What variable is unknown?")

    if unknownVariable == "a":
        B = eval(input('What is B equal to?'))
        yesNo =input("Is this squared already? Enter yes or no")
        if yesNo == "Yes":
            B=B
        if yesNo == "No":
            B = B*B
        C = eval(input("Ok, now what is C equal to"))
        yesNo =input("Is this squared already? Enter yes or no")
        if yesNo == "Yes":
            C=C
        if yesNo == "No":
            C = C*C

        A = C - B
        print("A is equal to", math.sqrt(A))

    if unknownVariable == "b":
        A = eval(input('What is A equal to?'))
        yesNo =input("Is this squared already? Enter yes or no")
        if yesNo == "Yes":
            A=A
        if yesNo == "No":
            A = A*A

        C = eval(input("Ok, now what is C equal to"))
        yesNo =input("Is this squared already? Enter yes or no")
        if yesNo == "Yes":
            C=C
        if yesNo == "No":
            C = C*C

        C = A - B
        print("C is equal to", math.sqrt(C))

    if unknownVariable == "c":
        print('')
    else: print("Variable must be A B or C. Re-start the program")




main()
