from data import data
import random

print("Welcome to the higher lower game!")

# Chose 2 random entries from data and print them
def drawPair():
    should_continue = True
    person1 = random.choice(data)

    while should_continue:
        person2 = random.choice(data)
        if person1["name"] != person2["name"]:
            should_continue = False

    return person1, person2

# Check higher lower
def checkHigherLower(people_to_compare):
    more_follower = 1
    if people_to_compare[0]['follower_count'] > people_to_compare[1]['follower_count']:
        more_follower = 0

    return more_follower

# Check if guess was correct
def checkGuess(guess, people_to_compare):
    more_follower = checkHigherLower(people_to_compare)
    if guess == 1 and more_follower == 0:
        return True
    elif guess == 2 and more_follower == 1:
        return True
    else:
        return False


keep_playing = True
score = 0

while keep_playing:

    # Get user guess
    people_to_compare = drawPair()
    person1 = people_to_compare[0]
    person2 = people_to_compare[1]
    print(f"{person1['name']} ({person1['description']} from {person1['country']}) vs {person2['name']} ({person2['description']} from {person2['country']})")
    guess = int(input("Who has more followers? '1' or '2': "))
    was_correct = checkGuess(guess, people_to_compare)

    if was_correct:
        score += 1
        print("You were right! ")
        print(f"{people_to_compare[0]['name']}: {people_to_compare[0]['follower_count']}m followers")
        print(f"{people_to_compare[1]['name']}: {people_to_compare[1]['follower_count']}m followers")
        print(f"Your score: {score}")
    else:
        print(f"{people_to_compare[0]['name']}: {people_to_compare[0]['follower_count']}m followers")
        print(f"{people_to_compare[1]['name']}: {people_to_compare[1]['follower_count']}m followers")
        keep_playing = False

print(f"Game Over 🙃. You scored: {score} 🥳")
