##Bouqet Builder App

##Shop class
class Store
##the class that would be the blueprint for the shop object

    """
    constructor for the class that would include information stored about the store:
    -store inventory
    -item prices
    -player's money
    """
    def _init_ (self, inventory, prices, player_money):
        self.inventory = inventory
        self.prices = prices
        self.player_money = player_money

    """
    Methods that are actions the shop is responsible for:
    -display interview
    -purchase an item
    """
    def display_inventory(self)
        if self.inventory is None:
        print("The shop has no inventory!")
        else:
        print(self.inventory)

    def purchase_item(self, item):
        if item not in self.inventory:
            print("That item is not available!")
            return
        item_price = self.prices[item]
        if self.player_money < item_price:
            print("You do not have enough money!")
            return
        self.player_money -= item_price
        self.inventory.remove(item)
        print(f"You purchased {item}!")
        print(f"Money remaining: ${self.player_money}")