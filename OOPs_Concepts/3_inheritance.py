# Example B: Employee Management (Inheritance)
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def work(self):
        return f"{self.name} is working."

class Manager(Employee):
    def work(self):
        return f"{self.name} is managing the team."

class Developer(Employee):
    def work(self):
        return f"{self.name} is writing code."

class Tester(Employee):
    def work(self):
        return f"{self.name} is testing the application."

e1 = Manager("Alice", 80000)
e2 = Developer("Bob", 60000)
e3 = Tester("Charlie", 50000)

print(e1.work())
print(e2.work())
print(e3.work())
