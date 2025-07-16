"""
username: xv24324
student ID: 2411243
"""
def get_int(prompt):
    """
    Prompts the user to enter an integer.

    Parameters:
    - prompt (str): The prompt message to display to the user.

    Returns:
    int: An integer entered by the user.
    """
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input, please enter an integer.")

def get_quarters_int(prompt):
    """
    Prompts the user to enter a number of quarters.

    Parameters:
    - prompt (str): The prompt message to display to the user.

    Returns:
    int: A positive integer entered by the user.
    
    Special Cases:
    - number of quarters default 8.
    """
    while True:
        try:
            value = input(prompt)
            if value.isdigit() and int(value) > 0:
                return int(value)
            if not value:
                print("Default 8 quarters")
                return 8 # Simulation default 8 quarters.
            else:
                print("Invalid input, please enter a positive number.")
        except ValueError:
            print("Invalid input, please enter a positive number.")
                
            
        except ValueError:
            print("Invalid input, please enter a positive number.")

def get_non_negative_int(prompt):   
    """
    Prompts the user to enter a non-negative integer.

    Parameters:
    - prompt (str): The prompt message to display to the user.

    Returns:
    int: A non-negative integer entered by the user.
    """
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                print("Please enter a non-negative number.")
            else:
                return value
        except ValueError:
            print("Invalid input, please enter a number.")
                        
def get_vendor_choice(prompt):
    """
    Prompts the user to enter 1 or 2 for a a vendor number.

    Parameters:
    - prompt (str): The prompt message to display to the user.

    Returns:
    int: A vendor number integer entered by the user.
    """
    while True:
        try:
            value = int(input(prompt))
            if value in [1,2]:
                return value
            else:
                print("Invalid input, please enter 1 or 2.")
        except ValueError:
            print("Invalid input, please enter a number.")
                               
def get_technician_name(prompt):
    """
    Prompts the user to enter a valid technician name.

    Parameters:
    - prompt (str): The prompt message to display to the user.

    Returns:
    str: A valid technician name.
    """
    while True:
        name = input(prompt).strip()
        if name:
            return name
        else:
            print("Name cannot be empty.")