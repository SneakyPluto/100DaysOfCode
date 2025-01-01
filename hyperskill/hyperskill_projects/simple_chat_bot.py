def get_int():
    try:
        return int(input())
    except ValueError:
        pass
        
def get_string():
    try:
        return input()
    except ValueError:
        pass
   
def greet(bot_name, birth_year):
    print(f"Hello! My name is {bot_name}.")
    print(f"I was created in {birth_year}.")


def remind_name():
    print("Please, remind me your name.")
    your_name = input()
    # reading a name
    print(f"What a great name you have, {your_name}!")

def get_remainders():
    r1 = get_int()
    r2 = get_int()
    r3 = get_int()
    return r1, r2, r3

def guess_age():
    print("Let me guess your age.")
    print("Enter remainders of dividing your age by 3, 5 and 7.")
    
    remainders = get_remainders()
    calculate_age(remainders)

def calculate_age(remainders):
    r1 = remainders[0]
    r2 = remainders[1]
    r3 = remainders[2]
    your_age = (r1 * 70 + r2 * 21 + r3 * 15) % 105
    print(f"Your age is {your_age} that's a good time to start programming!")
    
    print("Now I will prove to you that I can count to any number you want.")

def counting(n):
    i = 0
    while i <= n:
        print(f"{i} !")
        i += 1
    
def test_knowledge():
    print("Let's test your programming knowledge.")
    print("Why do we use methods?")
    print("""1. To repeat a statement multiple times.
2. To decompose a program into several small subroutines.
3. To determine the execution time of a program.
4. To interrupt the execution of a program.""")
    while (get_int() != 2):
        print("Please, try again.")
    print("Congratulations, have a nice day!")

    

bot_name = "Aid"
birth_year = "2023"

greet(bot_name, birth_year) 
remind_name()
guess_age()

counting(get_int())

test_knowledge()