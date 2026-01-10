"""
Phase 6
Financial Reports

1. Total Salary
2. Total Assets Value
3. Comprehensive Financial Value
4. Back to Main Menu
"""
from Assets import Hardware
from Emplyoees import Manager
from input_validation import get_menu_choice


def calculate_total_salary_expenditure(employees:dict):
    """
    Calculate total expenditure for all employees
    For Staff => Just Salary
    For Manager  => Salary + bonus

    Polymorphism: each object calculates its own cost
    :param employees:
    :return:
    """

    print()
    print("=" * 50)
    print("         Total Expenditure")
    print("=" * 50)
    print()

    if not employees:
        print("No employees found in the system")
        print()
        return

    total_expenditure = 0
    staff_count = 0
    manager_count =0

    print("Employees Breakdown: ")
    print('-' * 50)
    for employee in employees.values():
        if isinstance(employee, Manager):
            pay = employee.total_pay()
            manager_count += 1
            print(f'{employee.emp_name}(Manager) : ${pay:,.2f}')
        else:
            pay = employee.emp_salary
            staff_count += 1
            print(f'{employee.emp_name}(Staff) : ${pay:,.2f}')
        total_expenditure += pay

    print("-" * 50)
    print()
    print(f" Total Employees: {len(employees)} ")
    print(f"       - Manager: {manager_count} ")
    print(f"         - Staff: {staff_count} ")
    print()
    print(f" Total Monthly Salary Expenditure: Rs.{total_expenditure} ")
    print(f"  Annual Salary Expenditure: ${total_expenditure * 12:.2f} ")
    print()


def calculate_total_assets_value(assets:dict):
    """
    Calculate total assets value

    Uses the __add__ DUNDER Method to calculate total assets value
    Can add Hardware + Software seamlessly
    :param assets:
    :return:
    """
    print()
    print("=" * 50)
    print("         Total Assets Value")
    print("=" * 50)
    print()

    if not assets:
        print("No assets found in the system")
        print()
        return

    total_assets_value = 0
    hardware_count = 0
    software_count = 0
    hardware_value = 0
    software_value = 0

    print("Assets Breakdown: ")
    print('-' * 50)

    for asset in assets.values():
        value = asset.get_a_value
        print(f"{asset.get_a_name} ({asset.get_a_category}): ${value:,.2f} ")

        total_assets_value = total_assets_value + asset.get_a_value # __add__
        if isinstance(asset, Hardware):
            hardware_count += 1
            hardware_value += value
        else:
            software_count += 1
            software_value += value

    print('-' * 50)
    print()
    print(f"Total Assets: {len(assets)}")
    print(f"   -Hardware: {hardware_count} ({hardware_value:.2f})")
    print(f"   -Software: {software_count} ({software_value:.2f})")
    print()

    print(f" Total Assets Value: Rs.{total_assets_value:.2f}")
    print()


def generate_full_financial_report(employees:dict, assets:dict):
    print()
    print("=" * 50)
    print("         Financial Report")
    print("=" * 50)
    print()

    total_salary = 0
    total_assets_value = 0

    for employee in employees.values():
        if isinstance(employee, Manager):
            total_salary += employee.total_pay()
        else:
            total_salary += employee.emp_salary()
    for asset in assets.values():
        total_assets_value += asset.get_a_value

    print("Company Overview")
    print('-' * 50)
    print()
    print(f"Total Employees: {len(employees)}")
    print(f"Total Assets: {len(assets)}")
    print()

    print("Financial Summary")
    print('-' * 50)
    print(f" Monthly Salary Expenditure: {total_salary:.2f} ")
    print(f' Annual Salary Expenditure: {total_salary * 12:.2f} ')
    print(f' Total Assets Value: {total_assets_value:.2f} ')
    print()

    if employees:
        avg_salary = total_salary / len(employees)
        print(f"Average Employee Cost: {avg_salary:.2f} ")
    if assets:
        avg_assets_value = total_assets_value / len(assets)
        print(f"Average Asset Value: {avg_assets_value:.2f} ")

    # assets to Salary Ratio
    if total_salary > 0:
        ratio =   total_assets_value / total_salary
        print(f" Assets to Monthly Salary Ratio: {ratio:.2f} ")
        print()

    print('-' * 50)
    print()


    print("Detailed Employee Listing")
    print('-' * 50)
    if employees:
        for employee in employees.values():
            print(employee)
            print()

    print()

    print("Detailed Asset Listing")
    print('-' * 50)
    if assets:
        for asset in assets.values():
            print(asset)
            print()
    print()
# generate_full_financial_report({},{})

def financial_report_menu(employees:dict, assets:dict):
    print()
    while True:
        print()
        print("=" * 50)
        print("     Financial Report")
        print("=" * 50)
        print()
        print("1. Total Salary Expenditure")
        print("2. Total Assets Value")
        print("3. Generate Full Financial Report")
        print("4. Back to Main Menu")

        print()
        print("-" * 50)
        print()

        choice = get_menu_choice("(1-4)")

        match choice:
            case 1:
                calculate_total_salary_expenditure(employees)
                input("press enter to continue...")
            case 2:
                calculate_total_assets_value(assets)
                input("press enter to continue...")
            case 3:
                generate_full_financial_report(employees, assets)
                input("press enter to continue...")
            case 4:
                print()
                print("Going Back to main menu...")
                break
