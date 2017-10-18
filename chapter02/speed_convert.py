def main():
    metersPerSecond = eval(input("This program converts a value in meters per second to miles per hour.\nPlease enter a value in meters per second: "))
    if metersPerSecond < 0:
        print("Invalid input")
    else:
        milesPerHour = metersPerSecond *3600/1609.34
        #3600 seconds = 1 hour
        #1 mile = 1609.34 metres
        print(metersPerSecond, "meters per second is equal to", milesPerHour, "miles per hour")
main()
