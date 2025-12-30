#phase 1.2

class Assets:
    def __init__(self, a_id:str, a_name:str, a_category:str, a_value:float):
        self.__a_id = a_id
        self.__a_name = a_name
        self.__a_category = a_category
        self.__a_value = a_value

    @property
    def get_a_id(self):
        return self.__a_id

    @property
    def get_a_name(self):
        return self.__a_name

    @property
    def get_a_category(self):
        return self.__a_category

    @property
    def get_a_value(self):
        return self.__a_value

    # Assets deprecation

    def assets_deprecation(self, year):
        """ Calculate assets deprecation according to years by 10%"""
        return self.get_a_value * (100 / year)

    def get_details(self,):
        return f"Id: {self.get_a_id} | Name: {self.get_a_name} | Category: {self.get_a_category} | Value: {self.get_a_value}"

    def __str__(self):
        return self.get_details()

"""
Subclass => hardware =+ condition
Subclass => software =+ expiry date
"""


class Hardware(Assets):
    """Hardware asset - INHERITANCE"""

    def __init__(self, asset_id:str, name:str, value:float, condition:str = "Good"):
        super().__init__(asset_id, name, "Hardware", value)
        self.__condition = condition

    @property
    def condition(self):
        return self.__condition

    def get_details(self):
        return f"{super().get_details()} | Condition: {self.__condition}"


class Software(Assets):
    """Software asset - INHERITANCE"""

    def __init__(self, asset_id:str, name:str, value:float, expiry_date:str):
        super().__init__(asset_id, name, "Software", value)
        self.__expiry_date = expiry_date

    @property
    def expiry_date(self):
        return self.__expiry_date

    def get_details(self):
        return f"{super().get_details()} | Expires: {self.__expiry_date}"