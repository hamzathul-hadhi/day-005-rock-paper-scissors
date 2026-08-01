import random

choices = ["rock", "paper", "scissors"]

print("=== Rock Paper Scissors ===")

player = input("Choose rock, paper or scissors: ").lower()
computer = random.choice(choices)

print(f"\nYou chose: {player}")
print(f"Computer chose: {computer}")

if player == computer:
    print("It's a tie!")

elif (
    (player == "rock" and computer == "scissors") or
    (player == "paper" and computer == "rock") or
    (player == "scissors" and computer == "paper")
):
    print("You win!")

elif player in choices:
    print("Computer wins!")

else:
    print("Invalid choice.")