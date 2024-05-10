def get_valid_input(start, end):
    """Get a valid integer input from the user between start and end (inclusive)."""
    while True:
        try:
            user_guess = int(input("Enter a number: "))
            if start <= user_guess<= end:
                return user_guess
            else:
                print(f"Please enter a number between {start} and {end}.")
        except ValueError:
            print("Invalid input. Please enter a number.")
if __name__ == '__main__':
    print(get_valid_input(1, 100))

    

