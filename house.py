name = input("What's your name? ")

"""if name == "Harry" or name == "Hermoine" or name == "Ron":
    print("Griffindor")
elif name == "Draco":
    print("Slytherin")
else:
    print("Who? ")"""

match name:
    case "Harry" | "Hermoine" | "Ron":
        print("Griffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who? ")
