def provide_hint(user_guess, actual_number):
    """Provide a hint based on the difference between user_guess and actual_number."""
    if user_guess < actual_number:
        return "Too low!"
    else:
        return "Too high!"
    