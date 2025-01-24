
potential_dates = [
    {
        "name": "Sasha",
        "gender": "male",
        "age": 18,
        "hobbies": ["rock music", "art"],
        "city": "Berlin",
    },
    {
        "name": "Maria",
        "gender": "female",
        "age": 35,
        "hobbies": ["art"],
        "city": "Berlin",
    },
    {
        "name": "Daniel",
        "gender": "non-conforming",
        "age": 50,
        "hobbies": ["boxing", "reading", "art"],
        "city": "Berlin",
    },
    {
        "name": "John",
        "gender": "male",
        "age": 41,
        "hobbies": ["reading", "alpinism", "museums"],
        "city": "Munich",
    },
]

def select_dates(dates):
    saved = []
    for person in dates:
        if ( 
            person["age"] > 30
            and "art" in person["hobbies"]
            and person["city"] == "Berlin" 
            ):

            saved.append(person["name"])
    return ", ".join(saved)

print(select_dates(potential_dates))

