"""
username: xv24324
student ID: 2411243
"""
import math
class Supply:
    """
    Represents a supply used in the hatchery.
    Parameters:
    - name (str): The name of the supply.
    - main_capacity (int): The maximum capacity of the main warehouse.
    - aux_capacity (int): The maximum capacity of the auxiliary warehouse.
    - depreciation (float): The depreciation rate per quarter.
    - cost_per_unit (float): The cost per unit of the supply.
    """

    def __init__(self, name, main_capacity, aux_capacity, depreciation, cost_per_unit):
        self.name = name
        self.main_capacity = main_capacity
        self.aux_capacity = aux_capacity
        self.depreciation = depreciation
        self.cost_per_unit = cost_per_unit
        self.main_stock = main_capacity
        self.aux_stock = aux_capacity

    def apply_depreciation(self):
        """
        Applies depreciation to the supply stocks.

        Decreases the main and auxiliary stocks based on the depreciation rate.
        """
        # self.main_stock -= (math.ceil(self.main_stock * (self.depreciation)))
        # self.aux_stock -= int(math.ceil(self.aux_stock * float(self.depreciation)))
        main_depreciation = math.ceil(self.main_stock * self.depreciation)
        aux_depreciation = math.ceil(self.aux_stock * self.depreciation)
        # Ensure the stock does not go below zero
        self.main_stock = max(0, self.main_stock - main_depreciation)
        self.aux_stock = max(0, self.aux_stock - aux_depreciation)

