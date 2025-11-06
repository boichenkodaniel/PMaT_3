class Student:
    def __init__(self,surname, name, age):
        self.surname = surname
        self.name = name
        self.age = age
    def info(self):
        print(f"Студент:{self.surname} {self.name}, Возраст: {self.age}")
student1 = Student("Бойченко","Даниэль", 20)
student1.info()