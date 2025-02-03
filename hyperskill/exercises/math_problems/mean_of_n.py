work = []
total = 0

# Number of items in the list
user_runs = int(input())

for i in range(user_runs):
    user_appends = int(input())
    work.append(user_appends)

for j in work:
    total += j

print(total / user_runs)