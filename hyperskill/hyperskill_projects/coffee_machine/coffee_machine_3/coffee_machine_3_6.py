#Aquire the number of cups needed
water_ml = int(input("Write how many ml of water the coffee machine has: \n> "))

milk_ml = int(input("Write how many ml of milk the coffee machine has: \n> "))

coffee_beans_g = int(input("Write how many grams of coffee beans the coffee machine has:\n> "))

coffee_cups_needed = int(input("Write how many cups of coffee you will need:\n> "))


coffee_machine(water_ml, milk_ml, coffee_beans_g, coffee_cups_needed)

def coffee_req(cups):
    water = 200
    milk = 50
    coffee_beans = 15
    water *= cups
    milk *= cups  
    coffee_beans *= cups

def coffee_machine(water, milk, beans, cups):
    water_ = water
    milk_ = milk
    coffee_ = beans
    water *=  cups
    milk *= cups  
    coffee_beans *= cups
    if 


    print(f"""{water} ml of water
{milk} ml of milk
{coffee_beans} g  of coffee beans""")
coffee_machine(coffee_cups)