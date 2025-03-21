
class Person:
    def __init__(self,name,age,address,gender):
        self.name = name
        self.age = age
        self.address = address
        self.gender = gender
        self.__ssn = None   # Private Attribute

    def display_info(self):
        return f"Name: {self.name}, Age: {self.age}, Address: {self.address}"

        # Getter method for ssn
    def get_ssn(self):
        """
        Returns the Social Security Number (SSN) of the person.
        """
        return self.__ssn

        # Setter method for ssn
    def set_ssn(self, ssn):
        """
        Sets the Social Security Number (SSN) of the person.
        :param ssn: A 9-character string representing the SSN.
        :raises ValueError: If the SSN is not a 9-character string.
        """
        if isinstance(ssn, str) and len(ssn) == 9 and ssn.isdigit():
            self.__ssn = ssn
        else:
            raise ValueError("Invalid SSN. It must be a 9-digit string.")

    def role_duties(self):
        return "Adhere to school policies and guidelines"