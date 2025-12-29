import random

win = "you won :)"
lose = "you lost :("

options = ["rock", "paper", "scissors"]
computer = random.choice(options)
print("welcome to my rock paper scissors game")
print("rock = 1")
print("paper = 2")
print("scissors = 3")

player = input("please enter a choice ")
print()

if player == "1":
    player_choice = "rock"
    print("You picked: rock")
elif player == "2":
    player_choice = "paper"
    print("You picked: paper")
elif player == "3":
    player_choice = "scissors"
    print("You picked: scissors")
else:
    print("Invalid choice!")
    exit()
    
print(f"Computer picked: {computer}")

if player_choice == computer:
    print("tie :)")
elif (player_choice == "rock" and computer == "scissors"):
  print(win)
elif (player_choice == "paper" and computer == "rock"):
  print(win)
elif (player_choice == "scissors" and computer == "paper"):
  print(win)
else:
  print(lose)