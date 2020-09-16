import random
from time import sleep

#avalible items
print("CHOOSE A PLAY\n")
print("Rock");
print("Paper");
print("Scissors");
win_count1 = 0
win_count2 = 0
round_count = 0


while round_count <= 10: 
        print("------------------------------------------------------------------------------------")
        pc = ["Rock","Paper","Scissors"] 
        pc_choice = random.choice(pc)


        choice = (input("choose a number for Rock,Paper or Scissors\n"))
        print("------------------------------------------------------------------------------------")

        if(choice == "Rock"):
            print("Player 1 choice is ", choice)
        if(choice == "Paper"):
            print("Player 1 choice is ", choice)
        if(choice == "Scissors"):
            print("Player 1 choice is ", choice)
        #PC showing its play

        print("PC's choice is:",pc_choice)
        print("------------------------------------------------------------------------------------")
        #playing
        #TIE
        if(choice == pc_choice):
            print("TIE!")
            print("------------------------------------------------------------------------------------")

        #WIN:
        if(choice=="Rock" and pc_choice=="Scissors"):
            print("Player1 Wins")
            win_count1 = win_count1 +1
            print("win count for player 1 is ",win_count1)
            print("win count for PC is ",win_count2)
            print("------------------------------------------------------------------------------------")
        if(choice=="paper" and pc_choice=="Rock"):
            print("Player 1Wins")
            win_count1 = win_count1 +1
            print("win count for player 1 is ",win_count1)
            print("win count for PC is ",win_count2)
            print("------------------------------------------------------------------------------------")
        if(choice=="Scissors" and pc_choice=="Paper"):
            print("Player1 Wins")
            win_count1 = win_count1 +1
            print("win count for player 1 is ",win_count1)
            print("win count for PC is ",win_count2)
            print("------------------------------------------------------------------------------------")
        #LOSE:
        if(choice=="Rock" and pc_choice=="Paper"):
            print("PC WON, U lose")
            win_count2 = win_count2 +1
            print("win count for player 1 is ",win_count1)
            print("win count for PC is ",win_count2)
            print("------------------------------------------------------------------------------------")
        if(choice=="Paper" and pc_choice=="Scissors"):
            print("PC WON, U lose")
            win_count2 = win_count2 +1
            print("win count for player 1 is ",win_count1)
            print("win count for PC is ",win_count2)
            print("------------------------------------------------------------------------------------")
        if(choice=="Scissors" and pc_choice=="Rock"):
            print("PC WON, U lose")
            win_count2 = win_count2 +1
            print("win count for player 1 is ",win_count1)
            print("win count for PC is ",win_count2)
            print("------------------------------------------------------------------------------------")
        round_count = round_count +1
        print("Round count is:",round_count) 
        if win_count1 ==3:
            print("------------------------------------------------------------------------------------")
            print("PLAYER 1 WON 3 ROUNDS")
            sleep(2)          
            print("PLAYER 1 WINS !")
        if win_count2 ==3:
            print("------------------------------------------------------------------------------------") 
            print("PC WON 3 ROUND")
            sleep(2)
            print("PC WINS !")
