def reverse_seq(n):
    working = []
    for i in range(1, n+1):
        working.append(i)
    working.sort(reverse=True)
    return working
print(reverse_seq(5))

#You have passed all of the tests! :)