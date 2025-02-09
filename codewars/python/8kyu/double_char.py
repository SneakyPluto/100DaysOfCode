def double_char(s):
    temp = ''
    for char in s:
        temp += char+char
    return temp
#You have passed all of the tests! :)
print(double_char("1234!_"))