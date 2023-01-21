import json
import random

class Player:
    def __init__(self, name, money):
        self.name = name
        self.money = money
        self.properties = []

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
        if self.money < 0:
            print(f"{self.name} has gone bankrupt.")
            return True
        return False

class Property:
    def __init__(self, name, price, rent):
        self.name = name
        self.price = price
        self.rent = rent
        self.owner = None

class Game:
    def __init__(self):
        self.players = [
            Player("Peter", 16),
            Player("Billy", 16),
            Player("Charlotte", 16),
            Player("Sweedal", 16)
        ]
        self.player_index = 0
        self.properties = []
        self.property_index = 0
        self.load_board()

    def load_board(self):
        with open("board.json", "r") as file:
            data = json.load(file)
        for property in data["properties"]:
            self.properties.append(Property(property["name"], property["price"], property["rent"]))

    def next_player(self):
        self.player_index += 1
        if self.player_index >= len(self.players):
            self.player_index = 0
        return self.players[self.player_index]

    def next_property(self):
        self.property_index += 1
        if self.property_index >= len(self.properties):
            self.property_index = 0
        return self.properties[self.property_index]
    
    def play_game(self, rolls):
        for roll in rolls:
            player = self.next_player()
            print(f"{player.name} rolled a {roll}.")
            property = self.next_property()
            if property.owner is None:
                if player.money >= property.price:
                    player.buy_property(property)
                else:
                    print(f"{player.name} cannot afford to buy {property.name}.")
            else:
                color_owner = property.owner
                for prop in self.properties:
                    if prop.name.startswith(property.name.split()[0]) and prop.owner != color_owner:
                        color_owner = None
                        break
                if color_owner:
                    rent = property.rent * 2
                else:
                    rent = property.rent
                player.pay_rent(property.owner, rent)
            player
