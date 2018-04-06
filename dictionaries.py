# Creating a dictionary
fruit = {"apple": "A red fruit",
         "orange": "An orange citrus fruit",
         "pear": "A green fruit",
         "lemon": "A sour yellow citrus fruit",
         "lime": "A sour green citrus fruit"
         }

# Adding to an existing dictionary
fruit["tomatos"] = "Not a fruit, but a vegetable!"
print(fruit)

# Printing all the values in an existing dictionary
for val in fruit.values():
    print(val)


# Printing out a single key
print(fruit["apple"])
print("=" * 50)

# Reassign a new value to an existing key
fruit["apple"] = "A delicious red fruit to be eaten"
print(fruit)
print("=" * 50)

# Delete a key and value from an existing dictionary
del fruit["apple"]
print(fruit)
print("=" * 50)

# Looping through a dictionary
for item in fruit:
    print(item)

# Clearing a dictionary
fruit.clear()
print(fruit)

# Loop through fruits and retrieve the value of a key
# if the key is available within the dictionary, otherwise
# give an error message
while True:
    required_fruit = raw_input("What fruit would you like?: ")
    if required_fruit.lower() == "quit":
        print("Have a great day!")
        break
    if required_fruit in fruit:
        # Get a specified key's value within the fruit dictionary
        description = fruit.get(required_fruit)
        print(description)
        break
    else:
        print("We don't carry {0}".format(required_fruit))
        break

# Provide a response that will carry both true and false responses.
while True:
    dict_key = raw_input("Select a fruit: ")
    # True if dict_key was able to be grabbed
    # False if dict_key is not found
    response = fruit.get(dict_key, "Sorry, we do not carry " + dict_key)
    print(response)
    if dict_key in fruit:
        break

# Print all the values in fruit dictionary
for snack in fruit:
    print(fruit[snack])

# Print a loop through fruit 10 times
for i in range(10):
    for snack in fruit:
        print("{0} is {1}".format(snack, fruit[snack]))
    print("=" * 40)

# Listing the keys in the fruit dictionary,
# Sorting the list,
# Print the key with it's respective value
keys = list(fruit)
keys.sort()
for df in keys:
    print("{0} - {1}".format(df, fruit[df]))

# Same as the example above.
ordered_keys = sorted(list(fruit.keys()))
for f in ordered_keys:
    print("{0} - {1}".format(f, fruit[f]))

# Same as the two above
for f in sorted(fruit.keys()):
    print("{0} - {1}".format(f, fruit[f]))

# Creating a dictionary as a tuple
f_tuple = tuple(fruit.items())
print(f_tuple)
print("=" * 40)
# Print a list of tuples
print(fruit.items())

# Unpacking the tuple
for item in f_tuple:
    fruit, desc = item
    print("{0} - {1}".format(fruit, desc))
