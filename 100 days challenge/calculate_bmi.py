def calculate_bmi():
  try:
    #Get user input
    height = float(input("Enter your height: "))
    weight = float(input("Enter your weight: "))

    #Check if the input is positive
    if height <0 or weight <0:
      print("Please enter positive value")
      return

    #Calculate BMI
    bmi = weight/(height ** 2)
    print(f"Your BMI is: {bmi:.2f}")

    # Details result
    if bmi < 18.5:
        print("You are underweight.")
    elif 18.5 <= bmi < 24.9:
        print("You have a normal weight.")
    elif 25 <= bmi < 29.9:
        print("You are overweight.")
    else:
        print("You are obese.")


  except ValueError:
    print("Invalid input. Please try again and enter numeric value")
  except ZeroDivisionError:
    print("Invalid input. Please try again and enter positive number")
  except Exception as e:
    print(f"An unexpected error occured {e}")

calculate_bmi()