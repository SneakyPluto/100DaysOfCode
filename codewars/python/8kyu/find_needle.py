def find_needle(haystack):
    # your code here
    for item in haystack:
        if item == "needle":
            item_index = haystack.index(item)
            return "found the needle at position " + str(item_index)
print(find_needle(["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"]))

#You have passed all of the tests! :)      