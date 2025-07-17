import random

rand = random.randint(1,5)
def user_input(n):
    while True:
        try:
            return int(input(n))
        except ValueError:
            print("❌ Please enter a valid integer.")

user = user_input("Enter value between 1-5: ")
if user > rand:
    print("Your value is bigger!")
elif user < rand:
    print("Your value is smaller!")
else:
    print("You match the number")



print("Computer number: ",rand)