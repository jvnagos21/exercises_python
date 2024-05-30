class Salary:
    def __init__(self, base, bonus):
        self.base = base
        self.bonus = bonus

    def annual_salary(self):
        return (self.base*12)+self.bonus
class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.aggregated_salary = salary
    def total_salary(self):
        return self.aggregated_salary.annual_salary()

salary = Salary(1000, 700)
emp = Employee('IU', 31, salary)
print(emp.total_salary())
