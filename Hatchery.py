"""
username: xv24324
student ID: 2411243
"""
from FishSpecies import FishSpecies
from Supply import Supply
from Technician import Technician
from utils import get_non_negative_int


class Hatchery:
    """
    Represents the hatchery and manages its operations.

    Attributes:
    - cash_balance (float): The current cash balance of the hatchery.
    - fixed_cost (float): The fixed costs (rent and utilities) per quarter.
    - technicians (list): List of hired technicians.
    - supplies (dict): Dictionary of supplies with their details.
    - fish_species (list): Dictionary of fish_species with their details.
    """

    def __init__(self):
        self.cash_balance = 10000 # Initial chash balance
        self.fixed_cost = 1500 # Fixed cost of each quarter
        self.technicians = [] # Create a list of hired technicians 
        self.supplies = {
            'Fertilizer': Supply('Fertilizer', 20, 10, 0.4, 0.10),
            'Feed': Supply('Feed', 400, 200, 0.1, 0.001),
            'Salt': Supply('Salt', 200, 100, 0.0, 0.001)
        } # Dictionary of supplies with their details.
        self.fish_species = [
            FishSpecies('Clef Fins', 0.1, 12, 2, 2, 250, 25),
            FishSpecies('Timpani Snapper', 0.05, 9, 2, 1, 350, 10),
            FishSpecies('Andalusian Brim', 0.09, 6, 2, 0.5, 250, 15),
            FishSpecies('Plagal Cod', 0.1, 10, 2, 2, 400, 20),
            FishSpecies('Fugue Flounder', 0.2, 12, 2, 2.5, 550, 30),
            FishSpecies('Modal Bass', 0.3, 12, 6, 3, 500, 50)
        ] # Dictionary of fish

    def hire_technician(self, name, rate, specialty=None):
        """
        Hires a new technician.

        Parameters:
        - name (str): The name of the technician.
        - rate (float): The weekly rate paid to the technician.
        - specialty (str, optional): The specialty fish species the technician can handle.

        Returns:
        None

        Special Cases:
        - Maximum of 5 technicians can be hired.
        - Technicians must have unique names.
        """
        # Make sure the number of technician less or equal to 5.
        if len(self.technicians) >= 5:
            print("Maximum number of technicians reached.")
            return
        # Check the name of technician whether it is already exist.
        while any(tech.name == name for tech in self.technicians):
            print("Technician with the same name already exists, please enter a different name.")
            # Recreate a different name if the name already exist.
            name = input("Enter technician's name: ").strip()
        # Add new technician into the technician list.
        self.technicians.append(Technician(name, rate, specialty))
        print(f"Hired {name}, weekly rate={rate}, specialty={specialty}")

    def fire_technician(self, name):
        """
        Fires an existing technician.

        Parameters:
        - name (str): The name of the technician to be fired.

        Returns:
        None

        Special Cases:
        - Prints a message if the technician is not found.
        """
        for tech in self.technicians:
            if tech.name == name:
                # Remove the choosed technician from the list
                self.technicians.remove(tech)
                print(f"Fired {name}, weekly rate={tech.rate}, specialty={tech.specialty}")
                return
        print(f"Technician named {name} not found.")

    def pay_technicians(self):
        """
        Pays the weekly wages to all hired technicians.

        Returns:
        None
        """
        # Compute the total wages of technicians in a quarter
        total_cost = sum([tech.rate * 12 for tech in self.technicians])  # Calculate total wage cost
        # Deduct the technician cost from cash balance.
        self.cash_balance -= total_cost
        print(f"Paid technician wages, total amount {total_cost}")

    def pay_fixed_costs(self):
        """
        Pays the fixed costs (rent and utilities).

        Returns:
        None
        """
        # Deduct the quarterly fixed cost from cash balance.
        self.cash_balance -= self.fixed_cost
        print(f"Paid rent and utilities {self.fixed_cost}")

    def pay_supply_costs(self):
        """
        Pays for the supplies used in the hatchery.

        Returns:
        None
        """
        total_cost = 0
        for supply in self.supplies.values():
            # Compute the cost of 2 warehouses.
            main_cost = supply.main_stock * supply.cost_per_unit
            aux_cost = supply.aux_stock * supply.cost_per_unit
            total_cost += (main_cost + aux_cost)
        # Deduct the supply cost from cash balance.
        self.cash_balance -= total_cost
        print(f"Paid supply costs, total amount {total_cost:.2f}")

    def apply_depreciation(self):
        """
        Applies depreciation to all supplies.

        Returns:
        None
        """
        for supply in self.supplies.values():
            supply.apply_depreciation()
        print("Applied supply depreciation.")

    def purchase_supplies(self, vendor_prices):
        """
        Purchases supplies from a vendor.

        Parameters:
        - vendor_prices (dict): Dictionary of vendor prices for each supply.

        Returns:
        bool: True if supplies were successfully purchased, False otherwise.

        Special Cases:
        - Insufficient funds will prevent the purchase.
        """
        total_cost = 0
        for supply in self.supplies.values():
            # Compute the required amount of supplyies in 2 warehouses.
            needed_main = supply.main_capacity - supply.main_stock
            needed_aux = supply.aux_capacity - supply.aux_stock
            # Compute the cost of supplyies in 2 warehouses.
            cost_main = needed_main * vendor_prices[supply.name]['main']
            cost_aux = needed_aux * vendor_prices[supply.name]['aux']
            total_cost += (cost_main + cost_aux)
            # Check whether cash balance can afford the supplies by comparing the cash with total cost of supplies.
            if self.cash_balance < total_cost:
                print(f"Insufficient funds to restock {supply.name}, need {total_cost:.2f} but only have {self.cash_balance:.2f}")
                print(f"Broke while restocking main warehouse in quarter {self.current_quarter}")
            supply.main_stock = supply.main_capacity
            supply.aux_stock = supply.aux_capacity
        self.cash_balance -= total_cost
        print(f"Purchased supplies, total amount {total_cost:.2f}")
        return True

    def sell_fish(self):
        """
        Sell fish to the market.

        Returns:
        None
        """
        total_sales = 0
        for fish in self.fish_species:
            # The maximum quantity of fish can be sold.
            max_sell = min(fish.demand, len(self.technicians) * 9 // fish.maintenance_time)
            quantity = get_non_negative_int(f"Fish {fish.name}, demand {fish.demand}, sell {fish.demand} (max {max_sell}): ")
            if quantity > 0:
                if self.check_and_deduct_resources(fish, quantity):
                    fish.demand -= quantity
                    total_sales += fish.price * quantity
                    print(f"Sold {quantity} {fish.name}, each priced at {fish.price}")
                else:
                    print(f"Insufficient resources to sell {quantity} {fish.name}")
        self.cash_balance += total_sales
        print(f"Total sales: {total_sales}")

    def check_and_deduct_resources(self, fish, quantity):
        """
        Checks and deducts the required resources for selling fish.

        Parameters:
        - fish (FishSpecies): The fish species being sold.
        - quantity (int): The number of fish to sell.

        Returns:
        bool: True if resources are sufficient, False otherwise.
        """
        # Requirement of supplies.
        required_fertilizer = fish.fertilizer * quantity
        required_feed = fish.feed * quantity
        required_salt = fish.salt * quantity
        # Check and deducts the fertilizer.
        if required_fertilizer > self.supplies['Fertilizer'].main_stock + self.supplies['Fertilizer'].aux_stock:
            return False
        elif required_fertilizer > self.supplies['Fertilizer'].main_stock:
            required_fertilizer -= self.supplies['Fertilizer'].main_stock
            self.supplies['Fertilizer'].main_stock = 0
            self.supplies['Fertilizer'].aux_stock -= required_fertilizer
        else:
            self.supplies['Fertilizer'].main_stock -= required_fertilizer

        # Check and deducts the feed.
        if required_feed > self.supplies['Feed'].main_stock + self.supplies['Feed'].aux_stock:
            return False
        elif required_feed > self.supplies['Feed'].main_stock:
            required_feed -= self.supplies['Feed'].main_stock
            self.supplies['Feed'].main_stock = 0
            self.supplies['Feed'].aux_stock -= required_feed
        else:
            self.supplies['Feed'].main_stock -= required_feed

        # Check and deducts the salt.
        if required_salt > self.supplies['Salt'].main_stock + self.supplies['Salt'].aux_stock:
            return False
        elif required_salt > self.supplies['Salt'].main_stock:
            required_salt -= self.supplies['Salt'].main_stock
            self.supplies['Salt'].main_stock = 0
            self.supplies['Salt'].aux_stock -= required_salt
        else:
            self.supplies['Salt'].main_stock -= required_salt

        return True

    def display_status(self):
        """
        Displays the current status of the hatchery.

        Returns:
        None
        """
        print(f"Hatchery name: Eastaboga, cash balance: {self.cash_balance:.2f}")
        for supply in self.supplies.values():
            # Status of 2 warehouses.
            print(f"Warehouse Main: {supply.name}, stock {supply.main_stock} (capacity={supply.main_capacity})")
            print(f"Warehouse Auxiliary: {supply.name}, stock {supply.aux_stock} (capacity={supply.aux_capacity})")
        for tech in self.technicians:
            # Status of technicians.
            print(f"Technician {tech.name}, weekly rate={tech.rate}, specialty={tech.specialty}")

