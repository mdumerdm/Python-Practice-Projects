import random

def NGG():
    print("Guessing land!")

    # Get range from the user
    while True:
        try:
            low_lim = int(input("Enter the lowest number for random number (e.g., 0): "))
            up_lim = int(input(f"Enter the highest number for random number (limit 10000): "))
            if low_lim < 0 or up_lim > 10000 or low_lim >= up_lim:
                print("Error, Enter valid range.")
                continue
            break
        except ValueError:
            print("Invalid input. Enter integers only.")

    # Get number of tries from the user
    while True:
        try:
            tot_tr = int(input("Enter the number of tries to guess (limit 100): "))
            if tot_tr < 1 or tot_tr > 100:
                print("Please enter a valid number of tries between 1 and 100.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")

    # Generate a random number in the specified range
    num_to_guess = random.randint(low_lim, up_lim)
    tries = 0

    print(f"I have selected a number between {low_lim} and {up_lim}. You have {tot_tr} tries to guess it.")

    # Start guessing loop
    while tries < tot_tr:
        try:
            guess = int(input(f"Try {tries + 1}: Enter your guess: "))
            if guess < low_lim or guess > up_lim:
                print(f"Your guess must be between {low_lim} and {up_lim}.")
                continue
            tries += 1

            if guess < num_to_guess:
                print("Too low!")
            elif guess > num_to_guess:
                print("Too high!")
            else:
                print(f"Congratulations! You guessed the number {num_to_guess} in {tries} tries!")
                return  # This return is now correctly indented
        except ValueError:
            print("Invalid input. Please enter an integer.")

    print(f"Sorry, you've used all your tries. The number was {num_to_guess}.")

if __name__ == "__main__":
    NGG()
