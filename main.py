"""
username: xv24324
student ID: 2411243
"""
from Hatchery import Hatchery
from utils import get_technician_name, get_vendor_choice, get_quarters_int, get_int


def main():
    """
    Main function to run the hatchery simulation.
    Returns:
    None
    """
    hatchery = Hatchery()
    # Prompt the user to enter the number of quarters
    num_quarters = get_quarters_int("Please enter number of quarters(default 8): ")
    # Dictionary of vendor information
    vendor_prices = {
        'Slippery Lakes': {
            'Fertilizer': {'main': 0.30, 'aux': 0.20},
            'Feed': {'main': 0.00010, 'aux': 0.00040},
            'Salt': {'main': 0.00005, 'aux': 0.00025}
        },
        'Scaly Wholesaler': {
            'Fertilizer': {'main': 0.20, 'aux': 0.20},
            'Feed': {'main': 0.00040, 'aux': 0.00040},
            'Salt': {'main': 0.00025, 'aux': 0.00025}
        }
    }
    
    # Start the simulation of each quarter.
    for hatchery.current_quarter in range(1, num_quarters + 1):
        print(f"{'=' * 32}\n======Simulating Quarter {hatchery.current_quarter}======\n {'=' * 32}")
        
        # Prompt the user to enter the change of technicain
        tech_change = get_int("To add enter positive, to remove enter negative, no change enter 0.\n>>> Enter number of technicians: ")
        # Check the input number of of technician change
        if tech_change == 0:  
            print("No technician change.")
        else:
            for _ in range(abs(tech_change)):
                if tech_change > 0:
                    # Hire new technician.
                    name = get_technician_name("Enter technician's name: ")
                    specialty = input("Does this technician have a specialty? (yes/no): ").lower() == 'yes'
                    if specialty:
                        # Add specialty for new hired technician.
                        fish_type = input("Enter specialty fish species: ")
                        hatchery.hire_technician(name, 500, fish_type)
                    else:
                        hatchery.hire_technician(name, 500)
                else:
                    # Choose which technician will be fired.
                    name = get_technician_name("Enter technician's name to remove: ")
                    hatchery.fire_technician(name)
                    
        # Sell fish to the market
        hatchery.sell_fish()
        # Pay the weekly wages to all hired technicians
        hatchery.pay_technicians()
        # Pays the fixed costs (rent and utilities)
        hatchery.pay_fixed_costs()
        # Pays for the supplies used in the hatchery.
        hatchery.pay_supply_costs()
        #Applies depreciation to the supply stocks.
        hatchery.apply_depreciation()
        
        # Choose vender to deliver the supplies.
        vendor_choice = get_vendor_choice(
"""List of Vendors
    1. Slippery Lakes
    2. Sclay Wholesaler
>>> Enter number of vendor to purchase from:""")
        if not hatchery.purchase_supplies(list(vendor_prices.values())[vendor_choice - 1]):
            break
        
        #Displays the current status of the hatchery.
        hatchery.display_status()
        print(f"END OF QUARTER {hatchery.current_quarter}")
        
        # Check the cash balance to determine the bankrupt.
        if hatchery.cash_balance < 0:
            print(f"Hatchery went bankrupt in quarter {hatchery.current_quarter}!")
            print(f"=== FINAL STATE quarter {hatchery.current_quarter + 1} ===")
            hatchery.display_status()
            break


if __name__ == "__main__":
    main()