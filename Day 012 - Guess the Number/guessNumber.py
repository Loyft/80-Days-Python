import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")

random_number = random.randint(1, 100)

should_continue = True
attempts_remaining = 6

while should_continue:
    guess = int(input(f"You have {attempts_remaining} attempts remaining: "))

    if guess > random_number:
        print("too high.")
        attempts_remaining -= 1
    elif guess < random_number:
        print("too low.")
        attempts_remaining -= 1
    elif guess == random_number:
        print(f"You win! {random_number} was the right guess! 🥳")
        should_continue = False

    if attempts_remaining == 0:
        print(f"You lose, you ran out of guesses 🙃, the right number was {random_number}")
        should_continue = False
