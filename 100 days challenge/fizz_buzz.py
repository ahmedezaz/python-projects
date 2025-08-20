try:
  #Ask user to enter number
  user_input = int(input("Enter number"))
  #logic to print FizzBuzz
  for i in range(1,user_input+1):
    #Check if the number is divisible by 3 and 5
    if i % 3 == 0 and i % 5 ==0:
      print("FizzBuzz")
    #Check if the number is divisible by 3
    elif i % 3 == 0:
      print("Fizz")
      #Check if the number us divisible by 5
    elif i % 5 == 0:
      print("Buzz")
    else:
      print(i)
except ValueError:
  print("Invalid input. Please enter a valid number")


