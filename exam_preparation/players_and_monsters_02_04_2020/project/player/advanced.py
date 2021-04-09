from project.player.player import Player


class Advanced(Player):
    HEALTH = 250

    def __init__(self, username: str):
        super().__init__(username, self.HEALTH)
