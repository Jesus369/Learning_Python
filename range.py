my_list = list(range(10))
print(my_list)

even = list(range(0, 10, 2))
odd = list(range(1, 10, 2))
print(even)
print(odd)
combinedNumbers = even + odd
combinedNumbers.sort()
print(combinedNumbers)

my_string = "abcdefghijklmnopqrstuvwxyz"
# Print the position of a letter
print(my_string.index("l"))
# Print a letter positioned at 11
print(my_string[11])

decimal = range(0, 100)
print(decimal)

my_range = decimal[3:40:3]
print(my_range)
print(my_range == range(3, 40, 3))

firstList = list(range(0, 5, 2))
secondList = list(range(0, 6, 2))
if (firstList == secondList):
    print("True")

answersInList = firstList + secondList
answersInList.sort()
print(answersInList)
answerList = []
for first in firstList:
    for second in secondList:
        answer = first + second
        answerList.append(answer)
print(answerList)

# Using the slice method
randomRange = range(0, 100)
# Reversing the order of range, decrementing by 2
print(randomRange[::-2])
# Incrementing by 2 from 0 - 100
print(randomRange[::2])
print(range(0, 50)[::5])

# Reverse the order of a sentence
reversedString = "!sehcihwdnas deen ew sehcihwdnas"
correctedString = reversedString[::-1]
print(correctedString)

o = range(0, 100, 4)
print(o)
# Slicing by 5 will multiply the 4, what was declared in o
# Incrementation will happen by 20's
p = o[::5]
print(p)
for i in p:
    print(i)
