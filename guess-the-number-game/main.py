import random

number = random.randint(1, 10)

for i in range(3):
    usernumber = int(input("Type number in a range 1 - 10\n"))
    if usernumber == number:
        print("Congratulations! You guess right")
        break
    elif i < 2:
        if usernumber > number:
            print("No, try again! \nThe number is lower\n")
        if usernumber < number:
            print("No, try again! \nThe number is higher\n")
    else:
        print("Unfortunately you didn't guess right, the number is: ", number)