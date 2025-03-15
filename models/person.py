
class Person:
    def __init__(self,name,age,address,gender):
        self.name = name
        self.age = age
        self.address = address
        self.gender = gender

    def display_info(self):
        return f"{self.name} {self.age} {self.address}"