user_score = 0
computer_score = 0

while True:
    # User Input
    user_choice = input("Choose rock, paper, or scissors: ").lower()

    # Computer Selection
    import random
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)

    # Game Logic
    if user_choice in choices:
        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}\n")

        if user_choice == computer_choice:
            print("It's a tie!")
        elif (
            (user_choice == "rock" and computer_choice == "scissors")
            or (user_choice == "scissors" and computer_choice == "paper")
            or (user_choice == "paper" and computer_choice == "rock")
        ):
            print("You win this round!")
            user_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1

        # Display Scores
        print(f"\nScores - You: {user_score} | Computer: {computer_score}\n")

        # Ask to Play Again
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing")
            break
    else:
        print("Invalid choice. Please choose rock, paper, or scissors.")


        