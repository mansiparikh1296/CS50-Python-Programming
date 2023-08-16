def main():
    # name = get_name()
    # house = get_house()
    student = get_student()
    # if student[0] == "Padma":
    #     student[1] = "Ravenclaw"
    if student["name"] == "Padma":
        student["house"] = "Ravenclaw"
    print(f"{student['name']} from {student['house']}")

# def get_name():
#     return input("Name: ")

# def get_house():
#     return input("House: ")    

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return {"name" : name, "house": house}
    # student = {}
    # student["name"] = input("Name: ")
    # student["house"] = input("House: ")
    



    # name = input("Name: ")
    # house = input("House: ")
    # # return (name, house) -->tuple (immutable)
    # return [name, house]  #list (mutable)

if __name__ == "__main__":
    main()