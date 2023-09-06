# We will write a rock paper scissors game in class - Complete it in this file
import random
import os

def get_choices():
    options = ["Rock", "Paper", "Scissors"]
    player_choice = player_choicee()
    computer_choice = random.choice(options)
    return {"player": player_choice, "computer": computer_choice}

def player_choicee():
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

def main():
    choices = get_choices()
    os.system('cls')
    print(f"{choices['player']} vs {choices['computer']}")

    options = ["Rock", "Paper", "Scissors"]
    num = [1, 2, 3]

    player_num = num[options.index(choices['player'])]
    comp_num = num[options.index(choices['computer'])]

    if(player_num == comp_num):
        print("It's a tie")
    elif(player_num == 1 and comp_num == 2):
        print("Computer Wins!")
    elif(player_num == 2 and comp_num == 3):
        print("Computer Wins!")
    elif(player_num == 3 and comp_num == 1):
        print("Computer Wins!")
    elif(comp_num == 1 and player_num == 2):
        print("You Win!")
    elif(comp_num == 2 and player_num == 3):
        print("You Win!")
    elif(comp_num == 3 and player_num == 1):
        print("You Win!")

main()