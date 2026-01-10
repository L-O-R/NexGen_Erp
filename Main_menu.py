from Assets import Hardware
from Emplyoees import Manager
from asset_menu import asset_management_menu
from company_financial import financial_report_menu
from employee_management import employee_management_menu
from input_validation import get_menu_choice


def save_employee_data(employees: dict, filename="employee.txt"):
    with open(filename, "w") as file:
        for employee in employees.values():
            if isinstance(employee, Manager):
                line = f"{employee.emp_id}|{employee.emp_name}|{employee.emp_role}|{employee.emp_salary}|{employee.bonus}\n"
            else:
                line = f"{employee.emp_id}|{employee.emp_name}|{employee.emp_role}|{employee.emp_salary}\n"
            file.write(line)
    return len(employees)


def save_asset_data(assets: dict, filename="asset.txt"):
    with open(filename, "w") as file:
        for asset in assets.values():
            if isinstance(asset, Hardware):
                line = f"{asset.get_a_id}|{asset.get_a_name}|{asset.get_a_category}|{asset.get_a_value}|{asset.condition}"
            else:
                line = f"{asset.get_a_id}|{asset.get_a_name}|{asset.get_a_category}|{asset.get_a_value}|{asset.expiry_date}"
        file.write(line)
    return len(assets)


def save_all_data(employees: dict, assets: dict):
    asset_count = save_asset_data(assets, filename="asset.txt")
    emp_count = save_employee_data(employees, filename="employee.txt")

    print("=" * 50)
    print("Data Saved Successfully")
    print(f"Employee Count: {emp_count}")
    print(f"Asset Count: {asset_count}")
    print("=" * 50)


def display_main_menu(user):
    """
    Display the main menu
    After every action the user returns over here
    :param user:dict
    :return: None
    """
    print()
    print("=" * 50)
    print(f"        Main Menu - Welcome, {user[0]}")
    print("=" * 50)
    print()
    print('1. Manage Employees')
    print('2. Manage Assets')
    print('3. Company Financial')
    print('4. Save & Exit')
    print()
    print('=' * 50)



def main_menu_loop(user, employees, assets):
    """
    main phase 3
    :param user:dict
    :param employees:dict
    :param assets: dict

    this is an infinite loop that keeps running until user chooses "Save & Exit"
    flow:
    1. Display the main menu
    2. Get user choice
    3. Execute the action
    4. Return to step 1(main menu)
    5. Only "Save & Exit" will break the loop
    :return: None
    """

    running = True
    while running:
        #display the menu
        display_main_menu(user)

        # get user choice
        choice = get_menu_choice("(1-4)", ('1', '2', '3', '4'))
        print()
        match choice:
            case 1:
                print("Loading Employees Management.... ")
                employee_management_menu(employees)
            case 2:
                print("Loading Assets Management.... ")
                asset_management_menu(assets, employees)

            case 3:
                print("Loading Company Financial.... ")
                financial_report_menu(employees, assets)
                input("Please enter to return to Main Menu")
            case 4:
                print("=" * 50)
                print("                Save & Exit")
                print("=" * 50)
                print()
                confirm = input("Do you wish to Exit? (y/n): ").strip()
                if confirm == "y" or confirm == "Y":
                    print()
                    print("Saving the data....")
                    save_all_data(employees, assets)
                    print("✅ System shutdown initiated  ")
                    running = False
                else:
                    print()
                    print("✅ Cancelled . Returning to Main Menu")

    return True



