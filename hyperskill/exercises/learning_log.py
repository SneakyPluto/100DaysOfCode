import math
x = int(input())
y = int(input()) #base

def log_calc(x, y):
    if (y <= 1):
        return round(math.log(x), 2)
    else:
        return round(math.log(x, y), 2)
    
print(log_calc(x, y))
