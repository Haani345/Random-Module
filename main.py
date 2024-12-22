import random
playing=True
num=str(random.randint(10,20))

while playing:
    guess=int(input("Enter the number between ten to twenty: "))
    if num==guess:
        print("You win the game")
        print("The number was",num)
        break
    else:
        print("The guess is not right try again")