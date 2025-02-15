def sum_array(a):
    total = 0
    if len(a) == 0:
        return 0
    else:
        for num in a:
            total += num
        return total
    
print(sum_array([-1]))
#You have passed all of the tests! :)