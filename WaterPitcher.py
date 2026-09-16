##Bouqet Builder App

##Water Pitcher Class
class WaterPitcher:
##the class that would be the blueprint for the water pitcher object

    """
    constructor for the class that would include information stored about the water pitcher:
    -water pitcher color
    -water pitcher pattern
    -water pitcher material
    -price
    -if purchased
    """
    def _init_ (self, pitcher_color, pitcher_pattern, pitcher_material, price, purchased):
        self.pitcher_color = pitcher_color
        self.pitcher_material = pitcher_material
        self.price = price
        self.purchased = purchased

    """
    No methods as the water pitcher does not the have ability to carry out actions
    """