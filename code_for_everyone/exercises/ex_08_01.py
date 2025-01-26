# Opens the romeo text file
with open('romeo.txt') as fh:
    #Empty list to hold the list of unique words
    unique_words = []
    #Reads each word in the file
    for line in fh:
        line = line.strip()
        line = line.split()
        for item in line:
            if item not in unique_words:
                unique_words.append(item)
        unique_words.sort()       
    print(unique_words)

# print(list_words)
#     line = line.rstrip()
#     words = line.split()
#     list_words.append(words)
#     if list_words[line] in list_words:
#         continue
#     else:
#         list_words.append(words)

# print(list_words.sort())