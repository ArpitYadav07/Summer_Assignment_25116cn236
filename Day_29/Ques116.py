# Inventory Management System
inventory = {}

while True:
    item = input("Item Name: ")
    qty = int(input("Quantity: "))

    inventory[item] = qty

    ch = input("Add more? (y/n): ")

    if ch == "n":
        break

print(inventory)