def find_even(n):
    i = 1
    while i < n:
        if i % 2 == 0:
            print(i)
        i += 1
x = int(input())
find_even(x)