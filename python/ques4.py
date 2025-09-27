# A company wants to maintain employee records in a file. Each record has
# emp_id, name, designation, salary. Write Python code to:
# - Add new employee records
# - Search for an employee by ID
# - Display all employees earning more than 50,000

import json

# Initialize empty employee records
employee_records = {}

def add_employee(emp_id, name, designation, salary):
    employee_records[emp_id] = {"name": name, "designation": designation, "salary": salary}
    with open("employees.json", "w") as file:
        json.dump(employee_records, file)

def search_by_id(emp_id):
    return employee_records.get(emp_id, "Employee not found")

def search_high_salary():
    return [emp for emp_id, emp in employee_records.items() if emp["salary"] > 50000]

# Example usage
add_employee("E001", "Alice", "Manager", 60000)
add_employee("E002", "Bob", "Developer", 40000)
print(search_by_id("E001"))
print(search_high_salary())