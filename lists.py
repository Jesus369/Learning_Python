# Count the number of instances for an IP Address
ipAddress = raw_input("Enter a valid address: ")
period = "."
if period not in ipAddress:
    print("Sorry this is not a valid IP Address")
else:
    print(ipAddress.count(".") + 1)

# Looping through activities
activities = ["baseball", "basketball", "hiking", "hocket"]
activities.append("cricket")
for a in activities:
    print("I like to engage myself in " + a)

# Sorting a list
evens = [22, 44, 6, 8, 10]
odds = [11, 3, 5, 77, 9]
sortedMergedList = odds + evens
# With .sort, you must use it on the original object
# Cannot mutate a new object
sortedMergedList.sort()
print(sortedMergedList)
newSortedList = sorted(sortedMergedList)
print(newSortedList)

# Create a list, consisting of 2 sublists.
numbers = [evens, odds]
print numbers

# Loop through a list of sublists, and the contents of sublists
for numbersSet in numbers:
    print(numbersSet)
    for value in numbersSet:
        print(value)

# sort a list of numbers in reversed order
numbersEven = [6, 2, 8, 4, 10]
numbersEven.sort(reverse=True)
print(numbersEven)

# List 2: Creates a list consisting of items/sentences
list_1 = ["Ham", "Turkey", "Bread", "Lettuce"]
# List 2: Creates a list iterating though each character of a string
list_2 = list("This is a list")
print("List 1: {0}".format(list_1))
print("List 2: {0}".format(list_2))

if list_1 == list_2:
    print("This is correct. They are the same type of list")
else:
    print("This is not correct! Different lists!")

# Create a list of many sublists
menuList = []
menuList.append(["spam", "egg", "bacon"])
menuList.append(["egg", "spam", "bacon", "spam"])
menuList.append(["spam", "spam", "egg"])
menuList.append(["egg", "bacon", "egg"])
menuList.append(["spam", "bacon", "spam", "spam", "egg"])

for meal in menuList:
    # if "bacon" not in meal /This will work too
    if not "bacon" in meal:
        print(meal)
        for ingredient in meal:
            print(ingredient)
