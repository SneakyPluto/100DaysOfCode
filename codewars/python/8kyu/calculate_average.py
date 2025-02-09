def find_average(numbers):
    # your code here
    if  numbers: 
        total = 0
        for i in numbers:
            total += i
        return total / len(numbers) 
    return 0
print(find_average([]))

#Alternative solution
def find_average(array):
    try:
        return sum(array) / len(array)
    except ZeroDivisionError:
        return 0