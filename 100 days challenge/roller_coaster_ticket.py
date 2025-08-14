#Title of the game
print("Welcome to Adventure Roller Coaster Fun Zone!!!")
#Enter user height
height = float(input("Enter your height: "))
#Variable for price
price = 0
#age and price checking function
def age_check(age):
    if age < 12:
        price = 5
        return price
    elif age >= 12 and age < 18:
        price = 7
        return price
    else:
        price = 12
        return price

#height check condition
if height >120:
    #Enter user age
    age = int(input("Enter your age: "))
    price_no_image = age_check(age)
    picture = input("Would you like picture with your ticket? Y/N: ")
    if picture == "y":
        picture_with_image = price_no_image + 3
        print(f"Your total price with picture is: {picture_with_image}")
    else:
        print(f"Your total bill is: {price_no_image}")

else:
    print("Sorry you can't ride. Height must be over 120cm. Thank you.")

