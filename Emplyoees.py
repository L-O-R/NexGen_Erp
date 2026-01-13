#Phase 1.1
class Employee:

    def __init__(self, emp_id:str, emp_name:str, emp_role:str, emp_salary:float):
        self.__emp_id = emp_id
        self.__emp_name = emp_name
        self.__emp_role = emp_role
        self.__emp_salary = emp_salary
        self.__assigned_assets = []

    @property
    def emp_id(self):
        return self.__emp_id

    @property
    def emp_name(self):
        return self.__emp_name

    @property
    def emp_role(self):
        return self.__emp_role

    @property
    def emp_salary(self):
        return self.__emp_salary

    @property
    def assigned_assets(self):
        return self.__assigned_assets


    # setter
    @emp_name.setter
    def emp_name(self, emp_name):
        self.__emp_name = emp_name

    @emp_role.setter
    def emp_role(self, emp_role):
        self.__emp_role = emp_role

    @emp_salary.setter
    def emp_salary(self, emp_salary):
        self.__emp_salary = emp_salary

    def assign_assets(self, assets):
        self.__assigned_assets.append(assets)




    def get_details(self):
        """
            prints the details of the employee
        :return: None
        """
        assigned_assets = ""
        if self.__assigned_assets:
            asset_names = [asset for asset in self.__assigned_assets]
            return f"Id: {self.emp_id} | Name: {self.emp_name} | Role: {self.emp_role} | Salary: {self.emp_salary}|{asset_names}"
        return f"Id: {self.emp_id} | Name: {self.emp_name} | Role: {self.emp_role} | Salary: {self.emp_salary}| No Assigned Assets"

    def __str__(self):
        return self.get_details()
    def __repr__(self):
        return self.get_details()


class Manager(Employee):
    def __init__(self, emp_id:str, emp_name:str, emp_role:str, emp_salary:float, bonus:float = 1000 ):
        super().__init__(emp_id, emp_name, emp_role, emp_salary)
        self.__bonus = bonus

    @property
    def bonus(self):
        return self.__bonus
    @bonus.setter
    def bonus(self, bonus):
        self.__bonus = bonus
    def get_details(self):
        base_details = super().get_details()
        return f"{base_details} | Bonus: {self.bonus}"

    def total_pay(self):
        return self.emp_salary + self.bonus
