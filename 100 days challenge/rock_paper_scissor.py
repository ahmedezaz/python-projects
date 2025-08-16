import random
#Title of the game
print("Welcome to rock paper scissors game with PYROBOT")
#User input
user = input("Enter your choice. Choose rock, paper or scissor: ").lower()
choice_list = ["rock","paper","scissor"]
#Computer randomly choosing
computer_choose = random.choice(choice_list)
#printing both choices
print(f"Pyrobot choose: {computer_choose}")
print(f"You choose: {user}")

#Validating input
if user not in choice_list:
    print("INVALID INPUT")
    exit()
#Comparing logics
elif (computer_choose == "paper" and user == "rock") or (computer_choose == "rock" and user == "scissor") or (computer_choose == "scissor" and user == "paper"):
    print(f"Computer choose {computer_choose} and {computer_choose} beats {user}. COMPUTER WINS!!!")
elif computer_choose == user:
    print("ITS A DRAW")
else:
    print(f"You choose {user} and {user} beats {computer_choose}. YOU WIN")


