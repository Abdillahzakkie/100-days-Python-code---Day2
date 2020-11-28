#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: You might need to do some research in Google to figure out how to do this.

print("Welcome to tip calculator!")
total_bill = float(input("What was the total bill? $"))
percent_tip = float(input("What percentage tip would you like to give? $"))
total_number_of_people = float(input("How many people to split the bill? "))

percent_tip_amount = total_bill * (percent_tip / 100)

amount = (total_bill + percent_tip_amount) / total_number_of_people

print(f"Each person should pay: {round(amount, 2)}")