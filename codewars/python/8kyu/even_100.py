#print all even numbers up to 100
empty_list = []
for i in range (1, 101):
    if i % 2 == 0:
        empty_list.append(i)
    
print(empty_list)