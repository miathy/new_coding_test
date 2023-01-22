class Player:
    def __init__(self, name, money):
        self.name = name
        self.money = money
        self.properties = []
        self.location = 0

    def pay_rent(self, player, rent):
        self.money -= rent
        player.money += rent
        print(f"{self.name} paid ${rent} rent to {player.name}.")
        
    def buy_property(self, property):
        self.money -= property.price
        self.properties.append(property)
        property.owner = self
        print(f"{self.name} bought {property.name} for ${property.price}.")
        
    def check_bankruptcy(self):
        if self.money <= 0:
            print(f"{self.name} has gone bankrupt.")
            return True
        return False
    def move(self, roll, board_length):
        if self.location + roll >= board_length:
            self.location += roll - board_length
        else:
            self.location += roll
        return self.location
