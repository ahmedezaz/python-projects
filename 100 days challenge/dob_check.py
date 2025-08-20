#import library for date and time
import datetime
#Create object for today's date
now = datetime.datetime.now()
#User input for date of birth
date_string = input("Enter date of birth: Please use DD-MM (e.g., 05-10).")
try:
  #Parsing input value from user
  parsing_date = now.strptime(date_string, "%d-%m")
except ValueError:
  print("❌ Invalid date format. Please use DD-MM (e.g., 05-10).")
  exit()  # Exit the program early

#Logic to compare birthday with tpday's date
if (parsing_date.day == now.day) and (parsing_date.month == now.month):
  print("Happy Birthday!!!")
else:
  print("Today is not your birth day.")

#Printing message
print(type(date_string))