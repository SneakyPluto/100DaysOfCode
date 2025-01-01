height = float(input("Enter your height in CM: "))
weight = float(input("Enter your weight in KG: "))

def bmi_calc(h, w):
    return (w / (h**2)) * 1000

print(bmi_calc(height, weight))

weight = 85
height = 1.85

bmi = weight / (height ** 2)

# 🚨 Do not modify the values above
# Write your code below 👇
if bmi < 18.5:
    print("underweight")
elif (bmi >= 18.5 and bmi < 25):
    print("normal weight")
elif bmi >= 25:
    print("overweight")