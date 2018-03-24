aList = ["dog", "cat", "hamster", "gerbil"]
myIterator = iter(aList)
print(myIterator)
# Going onto the next item in a list using next()
print(next(myIterator))
print(next(myIterator))
# Grabbing the index of a list
print(aList[2])
print(aList[3])

string = "Here we have a string!"
for char in string:
    print(char)
print("==========")
for char in iter(string):
    print(char)

print(len(string))

week = ["monday", "tuesday", "wednesday",
        "thursday", "friday", "saturday", "sunday"]

# Iterate through week with a for loop
for day in week:
    print(day)

# Iterate through week using an iter
weekIter = iter(week)
print("========")
for nextDay in range(0, len(week)):
    next_day = next(weekIter)
    print(next_day)
