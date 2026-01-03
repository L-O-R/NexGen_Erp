# =========================================================
# Phase 4 => employee Management
# =========================================================
from Emplyoees import Manager, Employee


# generate unique employee id
def generate_employee_id(employees:dict):
    """
    Generate employee id
    Logic:
    1. extract all numeric parts from employee file
    2. find the maximum number
    3. add 1 to create new id
    4. format as ES001, ES002, ES003....
    :param employees:dict
    :return: id
    """
    if not employees:
        return "ES001"

    existing_numbers = []
    for emp_id in employees.keys():
        # remove "ES" prefix
        num = int(emp_id.replace("ES", ""))
        existing_numbers.append(num)

    next_num = max(existing_numbers) + 1

    return f'ES{next_num}'



#validate name
def validate_name(text:str):
    while True:
        name = input(text).strip()
        if not name:
            print("Please enter a valid employee name")
        elif any(char.isdigit() for char in name):
            print("Please enter a valid employee name, It cannot contain digits")
        else:
            return name
def validate_role(text:str):
    while True:
        role = input(text).strip()
        if not role:
            print("Please enter a valid employee name")
        elif any(char.isdigit() for char in role):
            print("Please enter a valid employee name, It cannot contain digits")
        else:
            return role.lower()
def validate_number(text:str, min_val = 0):
    while True:
        number = float(input(text).strip())
        if number >= min_val:
            return number
        else:
            print(f"Please enter a valid number at least {min_val}")


def add_employee(employees):
    """
    Add new employee to the database
    flow:
    1. get employee details
    2. validate all inputs
    3. generate unique id
    4. create employee or Manager
    5. add to dictionary
    :param employees:dict
    :return:employees:dict
    """
    emp_id = generate_employee_id(employees)
    name = validate_name("Enter employee name: ")
    role = validate_role("Enter employee role: ")
    salary = validate_number("Enter employee salary: ", 10000)

    if role == "manager":
        bonus = validate_number("Enter employee bonus: ", 1000)
        employee = Manager(emp_id, name, role, salary, bonus)
    else:
        employee = Employee(emp_id, name, role, salary)

    employees[emp_id] = employee
    print(f"Employee {emp_id} added")
    print(f"{employee}")
    print()
    return employees
# create 3 more function => view all employees + update + delete

# merge them in employee_sub_menu function
# flow:
'''
    1. print/ display emplyoee sub menu
    2. get user choice
    3. choice execute => 
    4. if press 5 option that is back to main menu 
'''