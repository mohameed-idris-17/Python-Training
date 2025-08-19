# Example B: Employee Management (Inheritance)
# What’s being inherited: common attributes (name, salary) and the generic work behavior from the Employee base class.
# What’s specialized: each subclass (Manager, Developer, Tester) customizes the work method to reflect its unique role.
# What’s exposed: a unified interface (work) for all employee types, making it easy to treat them polymorphically.
# How it works conceptually: shared data and logic live in the parent, while child classes override only what’s different, reducing duplication and clarifying responsibilities.
# Why it matters: simplifies code maintenance, enables flexible extension for new roles, and ensures consistent handling of all employees.
# One-liner for interview: “Inheritance lets every employee share core features, but each role can override behaviors to fit its job—making the system both DRY and adaptable.
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
