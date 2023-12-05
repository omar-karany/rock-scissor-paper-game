import random

#write hello message and game explanation for user
username = input("please inter your name : ")
explain = "Rock, paper, scissors is a game where rock squishes scissors, scissors cut paper, and paper covers rock!, We each pick one and see who wins each round by these rules."
print(f"hello {username} in 'r, p, s' game. {explain}")


#ask user to input the choice from choices rock paper scissor
user_choice = input("plaese inter your choice like: r or p or s ")
game = ["r", "s", "p"]

#pc choose randome choice 
pc_choice = random.choice(game)


#test the input if invalid or not
if user_choice not in game:
    print(f"Tie! please try again {username}")
elif user_choice == pc_choice:
    print(f"Tie! please try again {username}")


#make if condition to check user win or lose
print(f"your choice is : {user_choice} ,pc choice is: {pc_choice}  ")
if user_choice == "r" and pc_choice == "s" or user_choice == "s" and pc_choice == "p" or user_choice == "p" and pc_choice == "r":
    print(f"congratulations {username} yoy win ")
else: print(f"{username} you lose please try again")
