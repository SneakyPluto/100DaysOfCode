input_n = int(input())

for _ in range(1, input_n+1):
    if _ % 3 == 0 and _ % 5 == 0:
        print("FizzBuzz")
        break
    elif _ % 3 == 0:
        print("Fizz")
    elif _ % 5 == 0:
        print("Buzz")
    else:
        print(_)
