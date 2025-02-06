def make_negative(number):
    temp = str(number)
    if temp.startswith("-"):
        n = int(temp)
        return n
    else:
        n = int(temp)
        return n * -1
    
print(make_negative(-5))
#You have passed all of the tests! :)
