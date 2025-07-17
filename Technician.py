"""
username: Yibai
student ID: 2411243
"""
class Technician:
    """
    Represents a technician hired by the hatchery.
    Parameters:
    - name (str): The name of the technician.
    - rate (float): The weekly rate paid to the technician.
    - specialty (str, optional): The specialty fish species the technician can handle.
    """

    def __init__(self, name, rate, specialty=None):
        self.name = name
        self.rate = rate
        self.specialty = specialty
