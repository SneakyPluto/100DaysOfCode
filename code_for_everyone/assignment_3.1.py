hours = float(input("Enter Hours: "))
rate = float(input("Enter hourly rate: "))


if hours > 40:
    regular_pay = 40 * rate
    overtime_pay = (hours - 40) * rate * 1.5
    total_pay = regular_pay + overtime_pay
    print(total_pay)
else:
    total_pay = hours * rate
    print(total_pay)    
