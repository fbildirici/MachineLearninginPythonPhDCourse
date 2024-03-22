import random
def guess_number_game():
    # Generate random nums
    random_number = random.randint(1, 100)
    print("I have chosen a number between 1 and 100. Try to guess it!")

    while True:
        # user guess
        user_guess = int(input("Your guess: "))

        # Check the guess
        if user_guess < random_number:
            print("Higher!")
        elif user_guess > random_number:
            print("Lower!")
        else:
            print("Congratulations! You guessed it right.")
            break
guess_number_game()
