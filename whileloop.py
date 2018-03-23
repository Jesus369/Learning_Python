# while number is less than 11, prompt the user to keep entering numbers
# Untill it is equal to or greater than 11
number = 0
triesTaken = 1
while number < 11:
    number = int(raw_input(
        "I'm guessing a range of numbers between x an y, and ranges from 1 - 20. Select only one number from that range: "))
    print("You have now taken {0} tries".format(triesTaken))
    triesTaken += 1
print("You guessed correctly! I was guessing a number greater than 10")

# The user must select a correct exit to break the while loop, or just
# enter "quit" to break the while loop
availableExit = ["east", "south east", "north west"]
chosenExit = ""
while chosenExit not in availableExit:
    chosenExit = raw_input("Choose a direction: ").lower()
    if chosenExit == "quit":
        print("Glad to have you play the game!")
        break
    print("You found your way out!")

# Give the user an unlimited amount of guesses until they guess the correct answer
import random
print("What is your name?: ")
name = raw_input("")

highest = 1000
answer = random.randint(1, highest)
print("Please guess a number between 1 - {0}, {1}".format(highest, name))
guess = ""

while guess != answer:
    guess = int(raw_input(""))
    if guess == 0:
        print("Thank you for playing {0}!".format(name))
    elif guess < answer:
        print("You must guess higher!")
    elif guess > answer:
        print("You must guess lower!")
    else:
        print("You've guessed correctly!")

