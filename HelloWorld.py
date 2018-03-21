name = raw_input("what is your name? ")

print("Thank you for participating " + name)

age = int(raw_input("How old are you " + name + "? "))

if age < 21:
    print("Please come back in {0} years!".format(21 - age))
else:
    print("Thank you. You are entered into the contest!")