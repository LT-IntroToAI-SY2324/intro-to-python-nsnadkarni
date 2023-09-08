# We will write a rock paper scissors game in class - Complete it in this file
import random
import os
import math

def get_choices():
    options = ["Rock", "Paper", "Scissors"]
    player_choice = player_choice1()
    computer_choice = random.choice(options)
    return {"player": player_choice, "computer": computer_choice}

def get_choices2():
    options = ["Rock", "Paper", "Scissors"]
    player_choice = random.choice(options)
    computer_choice = random.choice(options)
    return {"player": player_choice, "computer": computer_choice}

def player_choice1():
    options = ["Rock", "Paper", "Scissors"]
    options2 = ["rock", "paper", "scissors"]
    
    loop = True
    while(loop):
        try:
            sel = input("Rock, Paper, or Scissors \n").lower()
            sel = options[options2.index(sel)]
            loop = False
            return sel
        except:
            print("Invalid Choice")
            pass
    loop = True

def main(a: int, b: int):
    if(a == 0):
        choices = get_choices()
    else:
        choices = get_choices2()
    os.system('cls')
    if(b != 0):
        print(f"{choices['player']} vs {choices['computer']}")

    options = ["Rock", "Paper", "Scissors"]
    num = [1, 2, 3]

    player_num = num[options.index(choices['player'])]
    comp_num = num[options.index(choices['computer'])]

    if(player_num == comp_num):
        if(b != 0):
            print("It's a tie")
        if(a == 1):
            return 0
    elif(player_num == 1 and comp_num == 2):
        if(b != 0):
            print("Computer Wins!")
        if(a == 1):
            return -1
    elif(player_num == 2 and comp_num == 3):
        if(b != 0):
            print("Computer Wins!")
        if(a == 1):
            return -1
    elif(player_num == 3 and comp_num == 1):
        if(b != 0):
            print("Computer Wins!")
        if(a == 1):
            return -1
    elif(comp_num == 1 and player_num == 2):
        if(b != 0):
            print("You Win!")
        if(a == 1):
            return 1
    elif(comp_num == 2 and player_num == 3):
        if(b != 0):
            print("You Win!")
        if(a == 1):
            return 1
    elif(comp_num == 3 and player_num == 1):
        if(b != 0):
            print("You Win!")
        if(a == 1):
            return 1

    looper = True
    while(True):
        try:
            a = input("Play Again? Y/N \n")
            a = a.lower()
            if((a == "y" or a == "n")):
                break
            else:
                4 / 0
        except:
            print("Y/N only")
            pass

    if(a == "y"):
        os.system("cls")
        main(0, 1)

def alt(a: int, b: str):
    tie_counter = 0
    win_counter = 0
    loss_counter = 0
    for i in range(a):
        print(f"Iteration: {i}/{a}")
        if(b == "-s"):
            res = main(1, 0)
        else:
            res = main(1, 1)
        if(res == 0):
            tie_counter += 1
        elif(res == 1):
            win_counter += 1
        elif(res == -1):
            loss_counter += 1

    print(f"Ties: {tie_counter} Wins: {win_counter} Losses: {loss_counter}")
    target = int(a / 3)
    print(f"{abs(math.floor((tie_counter / target) * 100) -100 )}% off (ideal) for a tie {abs(math.floor((win_counter / target) * 100) - 100)}% off (ideal) for a win {abs(math.floor((loss_counter / target) * 100) - 100)}% off (ideal) for a loss")

os.system("cls")

a = input("Sim or Play? \n")
a = a.lower()
if(a == "play"):
    main(0, 1)
else:
    a = input("How many iterations of the sim? \n")
    a = int(a)
    b = input("Messages on or off? \n")
    b = b.lower()
    if(b == "on"):
        alt(a, "")
    else:
        alt(a, "-s")
