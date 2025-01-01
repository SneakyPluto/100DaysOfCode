# def factorial(n):
#     i = 1
#     while i < n:        
#         if (n > i):
#             n * n
#         print(n)


# def factorial_new(n):
#     i = 1
#     total = n
#     while i < n:
#         total -= 1
#         n *= total
#         i+= 1
#     return n

def fact(n):
    i = 1
    while i <= n:
        n * (n - i)
        i+= 1
    return n

print(fact(3))

#Iteration 1: i = 1, n = 3, total = 3 * 2 = 6

#Iteration 2: i = 2, n = 2 , total = 6 + (2 * 1) = 8

#Iteration 3: i = 3, n = 3, total = 32 + 6

#Iteration 4: i = 4, n = 2, total = 38 + 2

#Iteration 5: i = 5, n = 1, total = 40 + 0

