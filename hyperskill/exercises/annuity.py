import math
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-i1", "--ingredient_1", choices=["pasta", "rice", "potato",
                    "onion", "garlic", "carrot", "soy_sauce", "tomato_sauce"],
                    help="You need to choose only one ingredient from the list.")

# write your code here
loan_principal = int(input("Enter the loan principal: "))

print("""What do you want to calculate?
type "m" - for number of monthly payments,
type "p" - for the monthly payment:""")

user_input = input() 
if (user_input.lower() == "m"):
    monthly_payment = int(input("Enter mothly payment: "))
    #Calculates the time it takes in months to repay the loan
    repay_time = round((loan_principal / monthly_payment))
    print(f"""It will take {repay_time} months to repay the loan """)

elif (user_input.lower() == "p"):
    num_months = int(input("Enter the number of months: "))
    paymount_amount = math.ceil(loan_principal / num_months)
    total_paid_before_last =  (num_months - 1) * paymount_amount
    last_payment = loan_principal - total_paid_before_last
    if last_payment != num_months:
        print(f"""Your monthly payment = {paymount_amount} and last payment = {last_payment}.""")
    else:
        print(f"""Your monthly payment = {paymount_amount} """)
