import time

def main():

    print("This is a program that calculates the average of test scores")

    total = 0
    number_of_test_scores = 0

    score = (input("What is the score (Press enter to quit and calculate): "))
    while score != "":
        score = eval(score)
        total = total + score
        number_of_test_scores = number_of_test_scores + 1
        score = input("What is the next score? (Press enter to quit and calculate): ")
    #This loop adds together the scores and divides by the amount of scores
    time.sleep(0.5)
    print("\nAverage =", total / number_of_test_scores)

main()


