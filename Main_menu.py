from asset_menu import asset_management_menu
from employee_management import employee_management_menu
from input_validation import get_menu_choice


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
                print("THis will be implemented in phase 6")
                print()
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
                    print("✅ System shutdown initiated  ")
                    running = False
                else:
                    print()
                    print("✅ Cancelled . Returning to Main Menu")

    return True

