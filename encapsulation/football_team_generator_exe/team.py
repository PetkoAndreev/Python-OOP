class Team:

    def __init__(self, name, rating):
        self.name = name
        self.rating = rating
        self.players = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def rating(self):
        return self.__rating

    @rating.setter
    def rating(self, value):
        self.__rating = value

    @property
    def players(self):
        return self.__players

    @players.setter
    def players(self, value):
        self.__players = value

    def add_player(self, player):
        '''
        add_player(player: Player) - adds a new player to the team.
        •	If the player is already in the team, return "Player {name} has already joined"
        •	Add the player to the team and return "Player {name} joined team {team_name}"
        '''
        if player in self.__players:
            return f"Player {player.name} has already joined"
        self.__players.append(player)
        return f"Player {player.name} joined team {self.name}"

    def remove_player(self, player_name):
        '''
        remove_player(player_name: str) - removes a player by its given name
        •	Remove the player and return him
        •	If the player is not in the team, return "Player {player_name} not found"
        '''
        for player in self.__players:
            if player.name == player_name:
                self.__players.remove(player)
                return player
        return f"Player {player_name} not found"
