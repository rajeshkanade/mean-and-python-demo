employees = {}

def add_employee(emp_id, emp_name, emp_salary):
    employees[emp_id] = {
        "name": emp_name,
        "salary": emp_salary
    }

def get_employee_by_id(emp_id):
    if emp_id in employees:
        return employees[emp_id]
    else:
        return "Employee not found."

def get_high_salary_employees():
    print("\nEmployees earning more than 50,000:")
    for emp_id in employees:
        if employees[emp_id]['salary'] > 50000:
            print(f"ID: {emp_id}, Name: {employees[emp_id]['name']}, Salary: {employees[emp_id]['salary']}")

# --- Main program ---
n = int(input("Enter number of employees: "))

for i in range(n):
    print(f"\nEnter details for Employee {i+1}:")
    emp_id = input("Employee ID: ")
    emp_name = input("Employee Name: ")
    emp_salary = float(input("Employee Salary: "))
    add_employee(emp_id, emp_name, emp_salary)

# Display employees with salary > 50,000
get_high_salary_employees()

# Search employee by ID
emp_id_search = input("\nEnter employee ID to search: ")
print(get_employee_by_id(emp_id_search))
