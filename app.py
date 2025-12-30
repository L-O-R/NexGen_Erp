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
from read import read_data_from_assets, read_data_from_employees, read_data_from_login_cred


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

login_phase()
