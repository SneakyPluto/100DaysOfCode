def number_to_string(num):
    return str(num)
#You have passed all of the tests! :)

#Alternative solution
def number_to_string(num):
    try:
        return str(num)
    except:
        return None