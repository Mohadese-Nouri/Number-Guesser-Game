import random
import streamlit as st


# st.title(":heavy_check_mark: Guess a number")


def validate_input(user_guess):
    if not user_guess.isdigit():
        print("Invalid input. Please enter a number.")
        return False
    user_guess = int(user_guess)
    if user_guess > 100 or user_guess < 1:
        print("Your guess is out of range. Please enter a number between 1 and 100.")
        return False
    return True


def number_guesser():
    number = random.randint(1,100)
    score = 100

    while True:
        user_guess = input("Guess a number between 1 and 100")

        if user_guess == "q":
            print("Thanks for playing! Goodbye!")
            break
    
        if not validate_input(user_guess):
            continue

        user_guess = int(user_guess)
        if user_guess < number:
            print("Too low!")
            score -= 1
        elif user_guess > number:
            print("Too high!")
            score -= 1
        else:
            print(f"Congratulations! Your score is: {score}!")
            play_again = input("Would you like to play again? (y/n)")
            if play_again.lower() == "y":
                number_guesser()
            else:
                print("Thanks for playing! Goodbye!")
            break
        score = max(0, score)
    

if __name__ == "__main__":
    number_guesser()



