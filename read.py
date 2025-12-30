import os

from Assets import Hardware, Software
from Emplyoees import Manager, Employee


def read_data_from_employees(filename:str = "employees.txt"):
    employee_dict = {}
    if not os.path.exists(filename):
        print("Employee list does not exist. Starting from scratch.")
        return employee_dict
    with open(filename, "r") as file:
       for line in file:
           line = line.strip()
           if line != "":
               parts = line.split("|")
               employee_id = parts[0]
               employee_name = parts[1]
               employee_role = parts[2]
               salary = float(parts[3])
               if employee_role == "Manager":
                   emp_bonus = float(parts[4])
                   employee_dict[employee_id] = Manager(employee_id, employee_name, employee_role, salary, emp_bonus)
               else:
                   employee_dict[employee_id] = Employee(employee_id, employee_name, employee_role, salary)

    return employee_dict

def read_data_from_assets(filename:str = "assets.txt"):
    asset_dict = {}
    if not os.path.exists(filename):
        print("Asset list does not exist. Starting from scratch.")
        return asset_dict
    with open(filename, "r") as file:
        for line in file:
            line = line.strip()
            if line != "":
                parts = line.split("|")
                asset_id = parts[0]
                asset_name = parts[1]
                asset_type = parts[2]
                assets_value = float(parts[3])
                if asset_type == "Hardware":
                    asset_condition = parts[4]
                    asset_dict[asset_id] = Hardware(asset_id, asset_name,assets_value, asset_condition)
                else :
                    asset_expiry = parts[4]
                    asset_dict[asset_id] = Software(asset_id, asset_name, assets_value, asset_expiry)
    return asset_dict


def read_data_from_login_cred(filename:str = "login_cred.txt"):
    user_dict = {}
    if not os.path.exists(filename):
        print("Login cred list does not exist. ONly admin access allow(default username and password).)")
        user_dict["admin"] = ("a", 1234)
        return user_dict
    with open(filename, "r") as file:
        for line in file:
            line = line.strip()
            if line != "":
                parts = line.split("|")
                role = parts[0]
                username = parts[1]
                password = parts[2]
            user_dict[role] = (username, password)
    return user_dict