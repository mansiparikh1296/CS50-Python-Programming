"""students = {
        "Hermoine": "Griyffindor", 
        "Harry": "Griyffindor",
        "Ron": "Griyffindor",
        "Draco": "Slytherin",
}"""
students = [
    {"name":"Hermoine", "house": "Griffindor", "patronous":"Otter"},
    {"name":"Harry", "house": "Griffindor", "patronous":"Stag"},
    {"name":"Ron", "house": "Griffindor", "patronous":"Jack Russell Terrier"},
    {"name":"Draco", "house": "Slytherin", "patronous":None}
]
for student in students:
    print(student["name"], student["house"], sep=", ")

"""print(students[0])
print(students[1])
print(students[2])"""

"""for student in students:
    print(student)"""

"""for i in range(len(students)):
    print(i+1, students[i])
houses = ["Griyffindor", "Griyffindor", "Griyffindor", "Slytherin"]"""

"""print(Students["Hermoine"])
print(Students["Harry"])
print(Students["Ron"])
print(Students["Draco"])"""

"""for student in Students:
    print(student, students[student], sep=", ")"""