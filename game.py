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
        for property in data:
            if (property["type"]) == 'property':
                self.properties.append(Property(property["name"], property["price"], property["colour"]))

    def next_player(self):
        self.player_index += 1
        if self.player_index >= len(self.players):
            self.player_index = 0
        return self.players[self.player_index]

    def next_property(self,player,roll):
        index = player.move(roll, len(self.properties))
        return self.properties[index]
    
    def play_game(self, rolls):
        for roll in rolls:
            player = self.next_player()
            print(f"{player.name} rolled a {roll}.")
            property = self.next_property(player,roll)
            if property.owner is None:
                if player.money >= property.price:
                    player.buy_property(property)
                else:
                    print(f"{player.name} cannot afford to buy {property.name}.")
            else:
                color_owner = property.owner
                for prop in self.properties:
                    if prop.colour == property.colour and prop.owner != color_owner:
                        color_owner = None
                        break
                if color_owner:
                    rent = property.rent * 2
                else:
                    rent = property.rent
                player.pay_rent(property.owner, rent)
            if (player.check_bankruptcy()):
                break
        print("------GAME END-----")
        winning_player = self.players[0]
        for player in self.players:
            if player.money > winning_player.money:
                winning_player = player
            print(f'{player.name} has {player.money} remaining')
            print(f"{player.name} is on {self.properties[player.location].name}")
        print(f'{winning_player.name} has won')