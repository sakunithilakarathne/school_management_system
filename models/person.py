
class Person:
    def __init__(self,name,age,address,gender):
        self.name = name
        self.age = age
        self.address = address
        self.gender = gender

    def display_info(self):
        return f"Name: {self.name}, Age: {self.age}, Address: {self.address}"