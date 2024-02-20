inventory = ["shoes, 12, 29.99", "shirts, 20, 9.99", "sweatpants, 25, 15.00", "scarves, 13, 7.75"]

for item in inventory:
    # Split each item into name, quantity, and price
    name, quantity, price = item.split(', ')

    # Format and print each item
print("The store has {}, each for {} USD.".format(quantity + " " + name, price))
