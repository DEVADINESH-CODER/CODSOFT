import random

choices = ["rock", "paper", "scissors"]

user = input("Enter your choice (rock, paper, or scissors):") 
user.lower()
computer_choice = random.choice(choices)

print(f"You choose {user}. The computer choose {computer_choice}.")

if user == computer_choice:
    print("TIE retry! ")
elif (
    (user == "rock" and computer_choice == "scissors")
    or (user == "paper" and computer_choice == "rock")
    or (user == "scissors" and computer_choice == "paper")
   ) :
    print("You win!")
else:
    print("You lose")