def computepay(h, r):
    if h > 40:
        regular_pay = 40 * r
        overtime_pay = (h - 40) * r * 1.5
        total_pay = regular_pay + overtime_pay
        return total_pay
    else:
        return h * r

hours = float(input("Enter Hours: "))
rate = float(input("Enter hourly rate: "))


pay = computepay(hours, rate)
print("Pay", pay)
