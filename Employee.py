employees = []

for i in range(3):
    print(f"\nEmployee {i + 1}")
    name = input("Name: ")
    age = int(input("Age: "))
    salary = int(input("Salary: "))
    employees.append((name, age, salary))

print(employees)