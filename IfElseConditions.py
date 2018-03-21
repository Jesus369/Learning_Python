# Example 1
name = raw_input("what is your name? ")

print("Thank you for participating " + name)

age = int(raw_input("How old are you " + name + "? "))

if age < 21:
    print("Please come back in {0} years!".format(21 - age))
else:
    print("Thank you. You are entered into the contest!")


# Example 2

print("I'm guessing a number between 1 - 10. Which number am I guessing?")

guess = int(raw_input(""))

if guess < 5:
    print("Sorry your guess needs to be higher. Try again!")
    guess = int(raw_input(""))
    if guess == 5:
        print("Well done!")
elif guess > 5:
    print("Try again! This time guess a little lower!")
    guess = int(raw_input(""))
    if guess == 5:
        print("Well done! You've guessed correctly!")
else:
    print("Well done! Got it the first try!")

number = int(raw_input("Enter a number "))

if 21 <= number <= 31:
    print("Your age is between 21 and 31!")
else:
    print("You fall outside of the range!")


# Challenge 1
# Create a small program asking for the name
# And age of a person. If they are between the ages of
# 18 and 30 invite them in.

print("What is your name?")
name = raw_input("")
print("welcome {0}, and how old are you".format(name))
age = int(raw_input(""))

if 18 <= age <= 30:
    print("Welcome {0}, you have been invited!".format(name))
else:
    print("We apologize {0}, but you are not invited".format(name))
