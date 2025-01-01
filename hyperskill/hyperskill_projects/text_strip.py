print("""Starting to make a coffee
Grinding coffee beans
Boiling water
Mixing boiled water with crushed coffee beans
Pouring coffee into the cup
Pouring some milk into the cup
Coffee is ready! """)

# def formatter(typeface):
#     cleaned = ''.join(char for char in typeface if char.isalpha)

# chars = ["*","_","~","`,"]
# my_string = ", ".join(chars)

some_string = input()
cleaned_text = some_string.strip("*_~`")
print(cleaned_text)

