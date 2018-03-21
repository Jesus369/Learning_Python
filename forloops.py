# print the range from 1 - 20.
for i in range(1, 20):
    print ("i is now {0}".format(i))

# Using a for loop within the range
number = "9,223,372,854,775,807"
cleanedNumber = ""
for i in range(0, len(number)):
    if number[i] in "0123456789":
        cleanedNumber = cleanedNumber + number[i]

newNumber = int(cleanedNumber)
print("the number is now {0}".format(newNumber))

# Using a for loop without range
thisNumber = "1,456,457,879,235"
cleanerNumber = ""
anotherNewNumber = ""
for char in thisNumber:
    if char in "0123456789":
        cleanerNumber = cleanerNumber + char

anotherNewNumber = int(cleanedNumber)
print("the anotherNewNumber is now {0}".format(anotherNewNumber))

# Using a list with a for loop
for state in ["not Houston", "not Austin", "not San Antonio"]:
    print("This is {0}".format(state))

# Performing a skip within a for loop
for i in range(0, 100, 5):
    print("i is {0}".format(i))

# Multiplication with 2 for loops
for i in range(1, 10):
    for j in range(1, 13):
        print("{0} times {1} equals {2}".format(i, j, i*j))
    print("=====================")
