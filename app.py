#======================================================================
# NexGen ERP Project
#======================================================================

"""
Phase 1 => Boot up the data from the file
What happens here
1. Check if data files exist or not
2. If file exists => load the data and convert them from string/text to object
3. if files don't exists => start with empty python dictionary
4. Prepare the system for user interaction

"""
"""
Phase 2 => Login Screen 
 After the systems boots up , the users sees the Login Screen
What happens here
1. User is prompted for UserName and Password
2. System verify cred against stored data
3. User has maximum of 3 attempts
4. After 3 failed attempts => Systems Locks and shutdown
5. On Success => Move to Main Menu
THis is security. prevents unauthorized access
"""

"""
PHASE 3 => Display Menu:

After successful login, user sees the MAIN MENU.
What happens here:
1. Display 4 main options
2. User selects an option (1-4)
3. System executes the chosen action
4. After action completes → Return to Main Menu (LOOP)
5. Only "Save & Exit" breaks the loop

This is the CENTRAL HUB - all navigation starts here.
"""

"""
PHASE 4 => Employee Management:
-------------------
Employee Management Sub-Menu - Full CRUD Operations

What happens here:
1. User selects "Manage Employees" from Main Menu
2. Shows Employee Sub-Menu with 5 options
3. Add, View, Update, Delete employees
4. Generate unique IDs automatically
5. Return to Main Menu when done
This is where we implement CREATE, READ, UPDATE, DELETE (CRUD).
"""

from read import read_data_from_assets, read_data_from_employees, read_data_from_login_cred
from Main_menu import main_menu_loop
import os
# =========================================================
# Phase 1.4
# =========================================================

def startup_phase():
    print("=" * 50)
    print("NexGen ERP ")
    print("Booting the system.....")
    print("=" * 50)
    print()
    # data load
    employees_dict = read_data_from_employees('employees.txt')
    assets_dict = read_data_from_assets('assets.txt')
    return employees_dict, assets_dict

# =========================================================
# Phase 2.2
# =========================================================

def login_phase():
    print("=" * 50)
    print("               Login Required ")
    print("=" * 50)
    print()

    #verification
    user_dict = read_data_from_login_cred('login_cred.txt')

    #max attempts
    max_attempts = 3
    attempt_count = 1
    role = input("Please enter your role: ")
    while attempt_count <= max_attempts:
        print(f"Login attempt #{attempt_count} out of {max_attempts}")
        if role in user_dict:

            username = input("Username: ")
            if username == user_dict[role][0]:
                password = input("Password: ")
                if password == user_dict[role][1]:
                    print("Logged in successfully")
                    print(f"Welcome {username}({role}) in NexGen ERP")
                    return username, role
                else:
                    print("Wrong password")
                    attempt_count += 1
            else:
                print("Wrong username")
                attempt_count += 1
        else:
            print("Wrong Role")
            role = input("Please enter your role(again): ")
            attempt_count += 1
    return None


# =========================================================
# Phase 3.1
# =========================================================

# clear our terminal/console
def clear_screen():
    # if os.name == "nt":
    #     os.system("cls")
    # else:
    #     os.system("clear")
    os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == "__main__":
    employees_dict, assets_dict = startup_phase()
    user = login_phase()
    if user is None:
        print()
        print("Exiting system")

    exit_req = main_menu_loop(user, employees_dict, assets_dict)
    if exit_req:
        print()
        print("=" * 50)
        print("Thank you for using NexGen ERP")
        print("=" * 50)
        print()