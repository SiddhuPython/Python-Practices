class Students:
    def __init__(self, *quantity):
        self.quantity = quantity
    def __str__(self):
        return f"number of students {len(self.quantity)}"
class Student:
    def __init__(self, name:str, age:int, branch:str):
        self.name = name
        self.age = age
        self.branch = branch
St1 = Student("siddhu", 25, "ECE")
St2 = Student("Siddhartha", 24, "EEE")
print(Students(St1, St2))