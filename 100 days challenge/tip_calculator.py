print("Welcome to the TIP Calculator")
# Validating input values
while True:
    # Input for the bill, tip and number of people
    bill = input("What was the total bill? $")
    tip = input("How much TIP would you like to give? 10 12 or 15? $")
    how_many_people = input("How many people split the bill? ")
    try:
        bill_validate = float(bill)
        tip_validate = float(tip)
        how_many_people_validate = float(how_many_people)
        break
    except ValueError:
        print("One of the input is invalid. Please enter numbers only")

if tip_validate == 10 or tip_validate == 12 or tip_validate == 15:
    # Calculating the tip and the amount per person
    tip_calculation = ((bill_validate * tip_validate) / 100) + bill_validate
    print(tip_calculation)
    per_person = tip_calculation / how_many_people_validate
    # printing the result
    print(f"Each person needs to pay $: {per_person:.2f}")
else:
    print("Invalid tip percentage")



