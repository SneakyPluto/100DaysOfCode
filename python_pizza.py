print("Thank you for choosing Python Pizza Deliveries!")
size = input() # What size pizza do you want? S, M, or L
add_pepperoni = input() # Do you want pepperoni? Y or N
extra_cheese = input() # Do you want extra cheese? Y or N
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

final_bill = 0
if size == "S":
    final_bill += 15
    if add_pepperoni == "Y":
        final_bill += 2
    if extra_cheese == "Y":
        final_bill += 1
if size == "M":
    final_bill +=20
    if add_pepperoni == "Y":
        final_bill += 3
    if extra_cheese == "Y":
        final_bill += 1
if size == "L":
    final_bill +=25
    if add_pepperoni == "Y":
        final_bill += 3
    if extra_cheese == "Y":
        final_bill += 1

print(f"Your final bill is: ${final_bill}.")
