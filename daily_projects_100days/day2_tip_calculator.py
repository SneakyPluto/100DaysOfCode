print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

#Calculations
tip_percent = tip / 100 
total_tip_amount = bill * tip_percent
total_cost = ((bill / people)) * total_tip_amount

round(total_cost, 2)
print(f"Each person should pay: ${total_cost}")

