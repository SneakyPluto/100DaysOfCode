#Aquire the number of cups needed
coffee_cups = int(input("Write how many cups of coffee you will need:"))

print(f"For {coffee_cups} cups of coffee you will need: ")


def coffee_machine(cups):
    water = 200
    milk = 50
    coffee_beans = 15
    water *=  cups
    milk *= cups  
    coffee_beans *= cups

    print(f"""{water} ml of water
{milk} ml of milk
{coffee_beans} g  of coffee beans""")
coffee_machine(coffee_cups)