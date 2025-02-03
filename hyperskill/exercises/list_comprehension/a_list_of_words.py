# work with the preset variable `words`
words = ['Athena', 'Travis', 'Alex', 'avicci']
new_list = [word for word in words if word.startswith(('a', 'A'))]

print(new_list)
[0, 1, 2, 3, ]
[0, 2, 0, 2, ]