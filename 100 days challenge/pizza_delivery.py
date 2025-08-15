#Title of the app
print("Welcome to the pizza order with Python")
#User inputs
size = input("Select pizza size? s,m,l: ").lower()
pepperoni = input("Would you like extra pepperoni? y/n: ").lower()
cheese = input("would you like extra cheese? y/n: ").lower()
total = 0
#pizza size select
if size == "s":
    total = 15
elif size == "m":
    total = 20
elif size == "l":
    total = 25
else:
    print("Invalid input")

#Pepperoni select logic
if pepperoni == "y":
    total += 2
elif pepperoni != "n":
    print("Invalid input")
    exit()


#Cheese select logic
if cheese == "y":
    total += 1
elif cheese != "n":
    print("Invalid input")
    exit()

print(f"Your total bill is: £{total}")






