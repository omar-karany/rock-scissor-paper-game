import random

# Write hello message and game explanation for user
username = input("Please enter your name: ")
print(f"Hello {username} in 'r, p, s' game. Rock, paper, scissors is a game where rock squishes scissors, scissors cut paper, and paper covers rock!")

# Ask user to input the choice from choices rock, paper, scissor
user_choice = input("Please enter your choice (r, p, s): ")
pc_choice = random.choice(["r", "s", "p"])
game = ["r", "s", "p"]

# Test the input if it's invalid or not
if user_choice not in game or user_choice == pc_choice:
    print(f"Tie! Please try again, {username}")
else:
    # Make an if condition to check if the user wins or loses
    print(f"Your choice: {user_choice}, PC choice: {pc_choice}")
    print(f"Congratulations {username}, you win!" if (user_choice == "r" and pc_choice == "s") or (user_choice == "s" and pc_choice == "p") or (user_choice == "p" and pc_choice == "r") else f"{username}, you lose. Please try again.")