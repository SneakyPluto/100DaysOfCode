# line_1 = "X O X"
# line_2 = "O X O"
# line_3 = "X X O"

# for i in range (1):
#     print(line_1, line_2, line_3, sep=" ")

# write your code here
line = input()

print("---------")
# Print the first row with spaces and pipes
print("|", " ".join(line[0:3]), "|")

# Print the second row with spaces and pipes
print("|", " ".join(line[3:6]), "|")

# Print the third row with spaces and pipes
print("|", " ".join(line[6:9]), "|")
print("---------")