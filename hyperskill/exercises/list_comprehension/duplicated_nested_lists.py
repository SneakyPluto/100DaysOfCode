n = int(input())

matrix = []
for i in range(n):

    # create empty row (a sublist inside our list)
    matrix.append([])

    for j in range(1, 3): 
        matrix[i].append(j) 
print(matrix)

# [[1, 2] * n for item in range(n)]
# print(my_list)