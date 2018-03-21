# Using continue within a for loop
# Continue will ignore what is declared and move onto the next line
shoppingList = ["eggs", "ham", "cheese", "spam", "bread"]
for item in shoppingList:
    if item == "spam":
        print("no spam please")
        continue
    print("Buy {0}".format(item))

# Using a break to kill the for loop
anotherList = ["pepperoni", "pasta", "turkey", "mashed potatoes"]
for item in anotherList:
    if item == "turkey":
        break
    print("Purchase {0}".format(item))

# Declaring an item into a variable then break the loop
# Conserve from loading more data than needed
nasty_food_item = ""
items = ["sausage", "ham", "eggs", "spam", "mayonaise" "cheese"]
for item in items:
    if "spam" in item:
        nasty_food_item = item
        print("Please leave out {0}".format(nasty_food_item))
        break
    elif "spam" not in items:
        print("no spam? I'll have all toppings then!")
        break
