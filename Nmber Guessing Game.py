import random

class NumberGuessingGame:
    def __init__(self, lower_bound=1, upper_bound=100, max_attempts=10):
        """
        Initialize the number guessing game.

        Args:
            lower_bound (int): The lower bound for the random number.
            upper_bound (int): The upper bound for the random number.
            max_attempts (int): Maximum number of attempts allowed for the player.
        """
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        self.max_attempts = max_attempts
        self.secret_number = random.randint(self.lower_bound, self.upper_bound)

    def get_user_guess(self):
        """Prompt the user to enter a guess and validate the input."""
        while True:
            try:
                guess = int(input(f"Enter your guess ({self.lower_bound} - {self.upper_bound}): "))
                if self.lower_bound <= guess <= self.upper_bound:
                    return guess
                else:
                    print(f"Please enter a number within the range {self.lower_bound} to {self.upper_bound}.")
            except ValueError:
                print("Invalid input. Please enter an integer.")

    def play_game(self):
        """Main game loop where the player makes guesses."""
        print(f"Welcome to the Number Guessing Game!")
        print(f"I have selected a number between {self.lower_bound} and {self.upper_bound}.")
        print(f"You have {self.max_attempts} attempts to guess it.")

        for attempt in range(1, self.max_attempts + 1):
            print(f"\nAttempt {attempt} of {self.max_attempts}:")
            guess = self.get_user_guess()

            # Check the player's guess against the secret number
            if guess < self.secret_number:
                print("Too low! Try again.")
            elif guess > self.secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You've guessed the number {self.secret_number} in {attempt} attempts!")
                break
        else:
            print(f"Sorry, you've used all your attempts. The secret number was {self.secret_number}.")

if __name__ == "__main__":
    # Create a game instance and start playing
    game = NumberGuessingGame()
    game.play_game()