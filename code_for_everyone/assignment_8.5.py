fh = open("mbox-short.txt")
count = 0
# words_list = []
email_list = []
for line in fh:
    line = line.strip()
    if line.startswith('From '): continue
    words = line.split()
    print(words[1])
        

# for i in range(len(words)):
#     for j in words[i]:

print(words)
print("There were", count, "lines in the file with From as the first word")

