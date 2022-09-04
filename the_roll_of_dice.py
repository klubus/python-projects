import random

print("*** Welcome in The Roll Of Dice program! *** \n ->If you want to roll of dice type 1 \n ->If you want to exit "
      "type 2 \n")
while True:
    condition = (str(input("What you want to do? \n")))
    if condition == "1":
        print("Your number is:", random.randint(1, 6))
    elif condition == "2":
        print("Thank you for using The Roll Of Dice program.")
        break
    else:
        print("You typed a wrong key :( \n ->If you want to roll of dice type 1 \n ->If you want to exit "
              "type 2 \n ")
