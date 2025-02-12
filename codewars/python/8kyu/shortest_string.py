def find_short(s):
    # your code here
    stripped = s.split()
    l = [len(item) for item in stripped] # Get lengths of each word
    
    # Initialize target to starting num in list l
    target = l[0]

    # Iterate through all count values in l, compare to find the smallest
    for num in l:
        if num < target:
            target = num
        else:
            continue
    return target

#You have passed all of the tests! :)

print(find_short("testingggg the strip function"))