import random
print("WELCOME TO THE GAME IMPOSSIBLE-GAME WHICH WILL DEFEAT YOUR GUESSING POWER")
print("RULES ARE-")
print("1. This game is all about guessing the numbers from the asked range.")
print("1. You have to clear 5 levels.")
print("2. With passing each level you'll be getting 50 points.")
print("3. You will have 5 chances on first level and as you pass levels your chances will get deducted.")
print("")
print("Let's start.")
print("")
print("Level:1")
print("")
#level 1
random1 = random.randint(1,11)
win = False
Turns =5
points=50
while win==False:
    Your_guess = input("Guess a number between 1 and 10:")
    print("You have",Turns-1,"chances left")
    Turns=Turns-1
    if Turns==0:
        print("You Lost, Game is over")
        break
    elif random1==int(Your_guess):
        print("That was easy, You won this level!")
        print("Points: ",points)
        win == True
#level 2
        print("")
        print("Congratulations you have cleared Level:1")
        print("")
        print("you are good in guessing the number")
        print("")
        print("Now pass level:2")
        print("")
        turns=4
        random2 = random.randint(1,21)
        while win==False:
            Your_guess = input("Guess a number between 1 and 20:")
            print("You have",turns-1,"chances left")
            turns=turns-1
            if turns==0:
                print("You Lost, Game is over")
                break
            elif random2==int(Your_guess):
                print("You won this level!")
                print("Points: ",points+50)
                win == True
#level 3
                print("")
                print("Congratulations you have cleared Level:2")
                print("")
                print("Now pass level:3")
                print("")
                print("Careful, one small mistake and game over")
                print("")
                turns=3
                random3 = random.randint(1,31)
                while win==False:
                    Your_guess = input("Guess a number between 1 and 30:")
                    print("You have",turns-1,"chances left")
                    turns=turns-1
                    if turns==0:
                        print("You Lost, Game is over")
                        break
                    elif random3==int(Your_guess):
                        print("You won this level!")
                        print("Points: ",points+50)
                        win == True
#level 4
                        print("")
                        print("only 0.5% people have cleared this Level:3")
                        print("")
                        print("welcome to level:4")
                        print("")
                        print("only 1 out 1000 can clear this level.")
                        print("")
                        turns=2
                        random4= random.randint(1,41)
                        while win==False:
                            Your_guess = input("Guess a number between 1 and 40:")
                            print("You have",turns-1,"chances left")
                            turns=turns-1
                            if turns==0:
                                print("You Lost, better luck next time")
                                break
                            elif random4==int(Your_guess):
                                print("You won this level!")
                                print("Points: ",points+50)
                                win == True
#level 5
                                print("")
                                print("Congratulations you have cleared almost an impossible Level:4")
                                print("")
                                print("This is the last level, you have only 1 chance to guess the number.")
                                print("")
                                turns=1
                                random5 = random.randint(1,51)
                                while win==False:
                                    Your_guess = input("Guess a number between 1 and 50:")
                                    print("You have",turns-1,"chances left")
                                    turns=turns-1
                                    if turns==0:
                                        print("You Lost, Game is over")
                                        break
                                    elif random5==int(Your_guess):
                                        print("You are a real genius,you completed the whole game.")
                                        print("Points: ",points+50)
                                        win == True
                                        break
                                    else:
                                        if random5>int(Your_guess):
                                            print("Your Guess was low, Please enter a higher number.")
                                        else:
                                            print("your guess was high, please enter a lower number.")
                                break
                            else:
                                if random4>int(Your_guess):
                                    print("Your Guess was low, Please enter a higher number.")
                                else:
                                    print("your guess was high, please enter a lower number.")
                        break
                    else:
                        if random3>int(Your_guess):
                            print("Your Guess was low, Please enter a higher number.")
                        else:
                            print("your guess was high, please enter a lower number.")
                break
            else:
                if random2>int(Your_guess):
                    print("Your Guess was low, Please enter a higher number.")
                else:
                    print("your guess was high, please enter a lower number.")
        break                    
    else:
        if random1>int(Your_guess):
            print("Your Guess was low, Please enter a higher number.")
        else:
            print("your guess was high, please enter a lower number.")
