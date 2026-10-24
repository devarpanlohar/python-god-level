import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__(___)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

# Put them in a dict - this is pro move
arts = {"rock": rock, "paper": paper, "scissors": scissors}

choices = ["rock", "paper", "scissors"]

# Score
user_score = 0
computer_score = 0

while True:
    print("\n---Rock Paper Scissors - ASCII Edition---")
    print("rock/paper/scissors or q to quit.")
    user_choice = input("Your choice: ").lower()

    if user_choice == "q":
        print(f"User scored: {user_score}")
        print(f"Computer scored: {computer_score}")
        break

    if user_choice not in choices:
        print("Invalid input! Please type rock, paper, scissors, or q to quit.")
        continue

    computer_choice = random.choice(choices)

    print(f"Computer chose: {arts[computer_choice]}")
    print(f"\nYou chose: {arts[user_choice]}")

    wins_over = {"rock": "scissors", "scissors": "paper", "paper": "rock"}

    if user_choice == computer_choice:
        print("Tie!")
        print(f"User scored: {user_score}")
        print(f"Computer scored: {computer_score}")
    elif wins_over[user_choice] == computer_choice:
        print("You win this round!")
        user_score += 1
        print(f"User scored: {user_score}")
        print(f"Computer scored: {computer_score}")
    else:
        print("Computer wins this round!")
        computer_score += 1
        print(f"User scored: {user_score}")
        print(f"Computer scored: {computer_score}")
