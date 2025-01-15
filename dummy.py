
# try:
#     a = int(input())
#     b = int(input())
#     result = a / b
# except ZeroDivisionError:
#     print("The Error!")

# else:
#     print(result)
import random
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

#What is wrong with this line of code
random.randint(x) for x in nested_list

#Please explain this line of code in comparison to the one below
print([random.choice(x) for x in nested_list])

# Please explain this line of code and what it is doing
(random.choice(x) for x in nested_list)