#Your program should print two lines:
#The key of the minimum value, preceded by "min: "
#The key of the maximum value, preceded by "max: "
import operator

# The following line creates a dictionary from the input. Do not modify it, please
test_dict = {"a": 43, "b": 1233, "c": 8}

print(f"min: {min(test_dict, key=test_dict.get)}")
print(f"max: {max(test_dict, key=test_dict.get)}")
