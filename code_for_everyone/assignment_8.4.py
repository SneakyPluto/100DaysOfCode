fname = input("Enter file name: ")
fh = open(fname)
lst = list()
some_list = []
for line in fh:
    line.rstrip()
    some_list = line.split()

print(some_list)
