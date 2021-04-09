from project.player.player import Player


class PlayerRepository:
    def __init__(self):
        self.count: int = 0
        self.players: list = []

    def add(self, player: Player):
        # •	If a player exists with a name equal to the name of the given player,
        #   raise a ValueError with message "Player {username} already exists!".
        # •	Otherwise, add the player and increase the count.
        if player.username in [p.username for p in self.players]:
            raise ValueError(f'Player {player.username} already exists!')
        self.players.append(player)
        self.count += 1

    def remove(self, player: str):
        # Removes a player from the collection.
        # •	If the player is an empty string, raise a ValueError with message "Player cannot be an empty string!".
        # •	Otherwise, remove the player and decrease the count of players
        if not player:
            raise ValueError('Player cannot be an empty string!')
        player_to_remove = self.find(player)
        self.players.remove(player_to_remove)
        self.count -= 1

    def find(self, username: str):
        # Returns a player with that username.
        return [p for p in self.players if p.username == username][0]
