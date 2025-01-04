switch = False
while not switch:
    try:
        name, surname = input().split()
    except Exception:
        print("You need to enter exactly 2 words. Try again!")

    else:
        print(f"Welcome to our party, {name} {surname}")
        switch = True
