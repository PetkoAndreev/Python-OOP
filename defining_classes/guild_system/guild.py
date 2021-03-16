class Guild:
    def __init__(self, name):
        self.name = name
        self.players = []

    def assign_player(self, player):
        if not player.guild == "Unaffiliated" and not player.guild == self.name:
            return f"Player {player.name} is in another guild."
        elif player.guild == self.name:
            return f"Player {player.name} is already in the guild."
        else:
            self.players.append(player)
            player.guild = self.name
            return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name: str):
        result = [p.name for p in self.players]
        if player_name not in result:
            return f"Player {player_name} is not in the guild."
        else:
            del self.players[player_name.index(player_name)]
            return f"Player {player_name} has been removed from the guild."

    def guild_info(self):
        guild_stats = f"Guild: {self.name}\n"
        for p in self.players:
            guild_stats += p.player_info()
        return guild_stats
