from Assets import Software, Hardware
from input_validation import validate_name, validate_number, get_menu_choice
import datetime

def generate_assets_id(assets:dict):
    """
    Generate assets id
    Logic:
    1. extract all numeric parts from assets file
    2. find the maximum number
    3. add 1 to create new id
    4. format as ES001, ES002, ES003....
    :param assets:dict
    :return: id
    """
    if not assets:
        return "A001"

    existing_numbers = []
    for emp_id in assets.keys():
        # remove "A" prefix
        num = int(emp_id.replace("A", ""))
        existing_numbers.append(num)

    next_num = max(existing_numbers) + 1

    return f'A{next_num}'


def validate_asset_type():
    while True:
        asset_type = input("Please enter your asset type(Hardware/Software): ").strip().title()
        if asset_type not in ["Hardware", "Software"]:
            print('Please enter your asset type "Hardware" or "Software"')
            continue
        else:
            return asset_type

def add_asset(assets:dict):
    print()
    print("=" * 50)
    print("      Add New Asset")
    print("=" * 50)
    print()
    asset_id = generate_assets_id(assets)
    name = validate_name("Enter assets name: ")
    value = validate_number("Enter assets value: ")
    asset_type = validate_asset_type()
    if asset_type == "Hardware":
        condition = input("Enter Physical Condition(eg. Good, Fair): ").strip()
        if not condition:
            condition = "Good"
        asset = Hardware(asset_id, name, value, condition)
    else:
        expiry_date = input("Enter Expiry Date: ").strip()
        if not expiry_date:
            expiry_date = datetime.date.today()

        asset = Software(asset_id, name, value, expiry_date)
    assets[asset_id] = asset
    print()
    print(f" asset added successfully: {asset_id}")
    print(asset)
    print()


def view_all_assets(assets:dict):
    print()
    print("=" * 50)
    print("      View All Assets")
    print("=" * 50)
    print()

    if not assets:
        print("No assets found")
    else:
        print(f" Total Assets: {len(assets)}")
        for asset in assets.values():
            print(f" {asset}")
            print("-" * 50)
            print()


def assign_asset(assets:dict, employee_dict:dict):
    print()
    print("=" * 50)
    print("      Assign New Asset")
    print("=" * 50)
    print()

    if not assets:
        print("No assets found")
        return
    if not employee_dict:
        print("No employee found")
        return

    assets_id = input("Enter asset ID: ")

    if  assets_id not in assets:
        print(f" Asset with id {assets_id} not found")
        return

    employee_id = input("Enter employee ID: ")
    if employee_id not in employee_dict:
        print(f" Employee with id {employee_id} not found")
        return

    asset = assets[assets_id]
    employee = employee_dict[employee_id]

    employee.assign_assets(asset)
    print()
    print(f"Asset {assets_id} successfully assigned to Employee {employee_id}")
    print()
    print("Update Employee Details: ")
    print(employee)

    print()


def  calculate_asset_depreciation(assets:dict):
    print()
    print("=" * 50)
    print("      Calculate Asset Depreciation")
    print("=" * 50)
    print()
    if not assets:
        print("No assets found")
        return

    assets_id = input("Enter asset ID: ")
    if assets_id not in assets:
        print(f" Asset with id {assets_id} not found")
        return

    asset = assets[assets_id]
    years = validate_number("Enter Years: ", min_val=0)

    original_value = asset.get_a_value
    current_value = asset.assets_deprecation(years)
    depreciation_value = original_value - current_value
    print()
    print(f"Assets: {asset.get_a_name}")
    print(f"Original Value: {original_value}")
    print(f"Current Value: {current_value}")
    print(f"Depreciation Value: {depreciation_value}")
    print()


def asset_management_menu(assets, employee_dict):
    while True:
        print()
        print("=" * 50)
        print("      Asset Management Menu")
        print("=" * 50)
        print()

        print("1. Add New Asset")
        print("2. View All Assets")
        print("3. Assign Asset to Employee")
        print("4. Calculate Asset Depreciation")
        print("5. Back to Main Menu")
        print()

        choice = get_menu_choice("(1-5)", ('1', '2', '3', '4', '5'))

        match choice:
            case 1:
                add_asset(assets)
                input("Press Enter to continue...")
            case 2:
                view_all_assets(assets)
                input("Press Enter to continue...")
            case 3:
                assign_asset(assets, employee_dict)
                input("Press Enter to continue...")
            case 4:
                calculate_asset_depreciation(assets)
                input("Press Enter to continue...")
            case 5:
                print("Back to Main Menu")
                break
