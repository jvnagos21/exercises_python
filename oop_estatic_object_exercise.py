from datetime import date

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


    @classmethod
    def personAge (cls, name, year):
        return cls (name, date.today().year - year)
    @staticmethod

    def isOldAge(age):
        return age >= 18

person1 = Person('IU', 31)
person2 = Person.personAge('Haerin', 2006)

print(person1.age)
print(person2.age)
