import random
options=["rock","paper","scissor"]
user_choice=input("Choose from rock, paper and scissor: ")
computer_choice=random.choice(options)

print("The user choice is: ",user_choice)
print("The computer choice is: ",computer_choice)

if user_choice==computer_choice:
    print("The game is a tie")
elif user_choice=="rock" and computer_choice=="scissor":
    print("rock smashes scissor, user won the game")
elif user_choice=="paper" and computer_choice=="rock":
    print("paper covers rock, user won the game")
elif user_choice=="scissor" and computer_choice=="paper":
    print("scissor cuts paper, user won the game")
else:
    print("You lose, try again")