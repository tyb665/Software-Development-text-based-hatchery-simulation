"""
username: xv24324
student ID: 2411243
"""
class FishSpecies:
    """
    Represents species of fish the hatchery raised.

    Parameters:
    - name (str): The name of the fish species.
    - fertilizer (int): The amount of fertilizer required per fish.
    - feed (int): The amount of feed required per fish.
    - salt (int): The amount of salt required per fish.
    - maintenance_time (float): The time required to maintain a fish.
    - price (float): The selling price of a fish.
    - demand (int): The market demand for this fish species.
    """

    def __init__(self, name, fertilizer, feed, salt, maintenance_time, price, demand):
        self.name = name
        self.fertilizer = fertilizer
        self.feed = feed
        self.salt = salt
        self.maintenance_time = maintenance_time
        self.price = price
        self.demand = demand