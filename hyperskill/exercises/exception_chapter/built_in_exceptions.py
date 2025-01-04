try:
    a = int(input())
    b = int(input())
    result = a / b
except ZeroDivisionError:
    print("The Error!")

else:
    print(result)
