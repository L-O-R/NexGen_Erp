# =========================================================
# Phase 4 => employee Management
# =========================================================
from Emplyoees import Manager, Employee
from input_validation import get_menu_choice, validate_name, validate_role, validate_number


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


def view_all_employees(employees:dict):
    print()
    print("=" * 50)
    print("            All Employees")
    print("=" * 50)
    print()
    if not employees:
        print("No Employees found , Add some")
    else:
        print(f'Total employees : {len(employees)}')
        print("_" * 50)
        for employee in employees.values():
            print(employee)
            print("_" * 50)
            print()
    print()

# {
#     "E001":{
#         name:
#         role:
# salary:
#     }
# }

def update_employee(employees:dict):
    print("=" * 50)
    print("            Update Employee")
    print("=" * 50)
    print()
    if not employees:
        print("No Employees found , Add some")
        print()
        return

    emp_id = input("Enter your employee id: ")

    if emp_id not in employees:
        print(f"Employee {emp_id} not found")
        print()
        return

    employee_data = employees[emp_id]

    print()
    print("Current employee details")
    print(employee_data)
    print()
    print("What would you like to update?")
    print("1. Name")
    print("2. Salary")
    if isinstance(employee_data, Manager):
        print("3. Bonus")
    print()
    max_choice = ('1', '2', '3') if isinstance(employee_data, Manager) else ('1', '2')
    choice = get_menu_choice('(1-3)', max_choice)

    print()

    match choice:
        case 1:
            new_name = validate_name("Enter new name: ")
            employee_data.name = new_name
        case 2:
            new_salary = validate_number("Enter new salary: ")
            employee_data.salary = new_salary
        case 3:
            new_bonus = validate_number("Enter new bonus: ")
            employee_data.bonus = new_bonus
    print()
    print("Updated employee details: ")
    print(employee_data)
    print()


def delete_employee(employees:dict):
    print("=" * 50)
    print("            Delete Employee")
    print("=" * 50)
    print()

    if not employees:
        print("No Employees found , Add some")
        print()
        return
    emp_id = input("Enter employee id: ")

    if emp_id not in employees:
        print(f"Employee {emp_id} not found")
        print()
        return

    employee_data = employees[emp_id]
    print()
    print("Employee to be deleted: ")
    print(employee_data)
    print()
    confirm = input("Are you sure you want to delete this employee? (y/n) ").lower().strip()
    if confirm == "y" or confirm == "yes":
        del employees[emp_id]
        print(f"Employee {emp_id} deleted")
        print()
    else:
        print()
        print("Delete Cancelled")
    print()


def employee_management_menu(employee:dict):
    while True:
        print()
        print("=" * 50)
        print("            Employee Management")
        print("=" * 50)
        print()
        print("1. Add new employee")
        print("2. View all employees")
        print("3. Update employee details")
        print("4. Delete employee")
        print("5. Back to main menu")
        print("=" * 50)
        choice = get_menu_choice("(1-5)", ('1', '2', '3', '4', '5'))

        match choice:
            case 1:
                add_employee(employee)
                input("Press enter to continue...")
            case 2:
                view_all_employees(employee)
                input("Press enter to continue...")
            case 3:
                update_employee(employee)
                input("Press enter to continue...")
            case 4:
                delete_employee(employee)
                input("Press enter to continue...")
            case 5:
                print()
                print("going back to main menu")
                break




