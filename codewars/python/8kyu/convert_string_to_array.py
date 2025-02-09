def string_to_array(s):
    temp_list = []
    if s != '':
        temp_list = s.split()
        return temp_list
    else:
        return ['']
print(string_to_array(""))
#You have passed all of the tests! :)
#Alternative solution
def string_to_array(string=''):
    return string.split() if string else ['']