import random

global response, user_guess, fb, x, xg1


def repeat():
    global response, user_guess
    x = random.randint(1, 100)
    xtype = x % 2
    fb = ["Congratulations! You have amazing guessing powers!!", "You are off by just a few!", "You are too "
                                                                                               "far:(",
          "You are so so close!", "getting further! here is a hint: it is an even number!",
          "Close! here is a hint: it is an even number!",
          "Further! here is a hint: it is an odd number!", "Close! here is a hint: it is an odd number!"]
    response = []
    i = 1
    while i <= 10:
        if i == 10 and x != user_guess:
            print("Oh oh! Seems like you are out of trials.\nThe number was " + str(x))
            i = 11
        elif response == fb[0]:
            i = 11
        else:
            user_guess = int(input("Guess the number:\n"))
            if user_guess == x:
                response = fb[0]
                print(response)
                i = 11
            elif user_guess > 100 or user_guess < 1:
                response = "Choose an integer between 1 and 100!"
                print(response)
            elif abs(x - user_guess) <= 2:
                response = fb[3]
                print(response)
            elif abs(x - user_guess) <= 5:
                if response == fb[3]:
                    response = "Oops! you are getting further! your last guess was closer"
                    print(response)
                else:
                    response = fb[1]
                    print(response)

            elif abs(x - user_guess) >= 40:
                if x > user_guess:
                    response = str(fb[2]) + "\nTry a bigger number!"
                    print(response)
                else:
                    response = str(fb[2]) + "\nTry a smaller number!"
                    print(response)

            else:
                if 1 < i <= 10 and (response == fb[1] or response == fb[3]):
                    response = "Nope! your last guess was closer!"
                    print(response)
                else:
                    if i <= 2:
                        if user_guess > x:
                            response = "You are getting closer! Try a smaller number"
                            print(response)
                        else:
                            response = "You are getting closer! Try a bigger number"
                            print(response)
                    elif 5 >= i > 2 and xtype == 0:
                        global xg1
                        if response == fb[1] or response == fb[3]:
                            response = "getting further! here is a hint: it is an even number!"
                            print(response)
                        elif (response == fb[4] or response == fb[5]) and xg1 == 0 and user_guess % 3 != 0:
                            print("No! here is another hint :it is divisible by 3")
                        elif (response == fb[4] or response == fb[5]) and xg1 != 0 and user_guess % 3 == 0:
                            print("No! here is another hint :it is not divisible by 3")
                        else:
                            response = "Close! here is a hint: it is an even number!"
                            print(response)
                    elif 5 >= i > 2 and xtype != 0:
                        xg1 = x % 3
                        if response == fb[1] or response == fb[3]:
                            response = "Further! here is a hint: it is an odd number!"
                            print(response)
                        elif (response == fb[6] or response == fb[7]) and xg1 == 0 and user_guess % 3 != 0:
                            print("No! here is another hint :it is divisible by 3")
                        elif (response == fb[6] or response == fb[7]) and xg1 != 0 and user_guess % 3 == 0:
                            print("No! here is another hint :it is not divisible by 3")
                        else:
                            response = "Close! here is a hint: it is an odd number!"
                            print(response)
                    else:
                        if user_guess < x:
                            xvalue1 = user_guess + abs(x - user_guess)
                        else:
                            xvalue1 = user_guess - abs(x - user_guess)
                        if 80 >= xvalue1 >= 20:
                            response = "Close! Here is another hint the number is between " + str(
                                xvalue1 - 20) + " and " + str(xvalue1 + 20)
                            print(response)
                        elif x < 20:
                            response = "Close! Here is another hint the number is between 0 and " + str(xvalue1 + 20)
                            print(response)
                        else:
                            response = "Close! Here is another hint the number is between " + str(
                                xvalue1 - 20) + " and 100"
                            print(response)
                    if i == 8 and user_guess != x and (response != fb[0] or response != fb[1] or response != fb[3]):
                        quitter = input("You are almost out of trials! do you want to quit now and reveal the number?\n"
                                        "Y or N:")
                        if quitter == "Y":
                            print("Aw! it is okay you can always try again.\nThe number was " + str(x))
                            repeat_feedback()
                        elif quitter == "N":
                            i = 8
                        else:
                            print("Please enter a valid answer!")
                            quitter_check()

        i += 1
    rf = input("Do you want to play another round?\nType Y or N: ")
    if rf == "Y":
        print("Hello again!")
        repeat()
    elif rf == "N":
        if response == fb[0]:
            print("Thank you for playing Pyguess!\nBe back soon, winner!")
        else:
            print("Thank you for playing Pyguess!\nBetter luck next time!")


def repeat_feedback():
    rf = input("Do you want to play another round?\nType Y or N: ")
    if rf == "Y":
        print("Hello again!")
        repeat()
    elif rf == "N":
        print("Thank you for playing Pyguess!")

    else:
        print("Please enter a valid answer!")


def quitter_check():
    quitter = input("You are almost out of trials! do you want to quit now and reveal the number?\n"
                    "Y or N:")
    if quitter == "Y":
        print("Aw! it is okay you can always try again.\nThe number was " + str(x))
        repeat_feedback()
    elif quitter == "N":
        i = 8
    else:
        print("Please enter a valid answer!")


print("Hi, there! Welcome to Pyguess:)")
name = input("Please enter your name here:\n")
print(
    "Hi," + name + ". Ready to test your guessing powers?""\nWe are generating a number for you between 1 and 100 to "
                   "guess right now!\nRemember you only"
                   " have 10 attempts to guess "
                   "it correctly\nIf not you can always try again and don't worry we will give you some hints along "
                   "the way!")
repeat()
