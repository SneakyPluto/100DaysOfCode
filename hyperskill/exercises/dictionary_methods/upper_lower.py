# the list with words from string
# please, do not modify it
all_words = []
for i in range(6):
    some_iterable = input().split()
    all_words.extend(some_iterable)
    
# use dictionary comprehension to create a new dictionary
new_dict = {key.upper(): key.lower() for key in all_words}
print(new_dict)

