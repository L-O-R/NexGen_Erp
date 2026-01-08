def get_menu_choice(max_choice:str,a:tuple = ("1", "2", "3", "4") ):
    """
    Get user choice with input validation
    :return:  choice
    """
    while True:
        choice = input(f"Enter your choice{max_choice}: ").strip()
        # if choice >= '1' and choice <= '4':
        if choice in a:
            return int(choice)
        else:
            print(f"❌ Invalid Choice! Please enter a number between {max_choice}.")

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