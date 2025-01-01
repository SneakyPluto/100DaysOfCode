bubblegum = 202
toffee = 118
ice_cream = 2250
milk_choc = 1680
dougnut = 1075
pancake = 80

total_revenue = bubblegum + toffee + ice_cream + milk_choc + dougnut + pancake


print(f"""Earned amount:
Bubblegum: ${bubblegum}
Toffee: ${toffee}
Ice cream: ${ice_cream}
Milk chocolate: ${milk_choc}
Doughnut: ${dougnut}
Pancake: ${pancake}

Income: ${total_revenue}""")

#Main staff expenses
print("Staff expenses: ")
staff_expenses = int(input())

print("Other expenses: ")
#Other expenses
other_expenses = int(input())
net_income = total_revenue - (staff_expenses + other_expenses) 

#Some calculation
print(f"Net income ${net_income}")