# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
values = []

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    
    #Extract the string
    full_string = line
    value = full_string[20:26]

    # Convert the extracted string to a float and append it to the list
    values.append(float(value))
    
total = 0
for num in values:
    total += num

# Calculate the average
avg = total / len(values)
print(f"Average spam confidence: {avg}")