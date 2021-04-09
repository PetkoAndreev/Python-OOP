from project.battle_field import BattleField
from project.card.card_repository import CardRepository
from project.card.magic_card import MagicCard
from project.card.trap_card import TrapCard
from project.player.advanced import Advanced
from project.player.beginner import Beginner
from project.player.player_repository import PlayerRepository


class Controller:
    def __init__(self):
        self.player_repository: PlayerRepository = PlayerRepository()
        self.card_repository: CardRepository = CardRepository()

    def add_player(self, type_p: str, username: str):
        # Creates a player with the provided type and name. The method should return the following message:
        # "Successfully added player of type {type} with username: {username}"
        if type_p == 'Beginner':
            self.player_repository.add(Beginner(username))
        elif type_p == 'Advanced':
            self.player_repository.add(Advanced(username))
        return f'Successfully added player of type {type_p} with username: {username}'

    def add_card(self, type_c: str, name: str):
        # Creates a card with the provided type -> "Magic" or "Trap" and name.
        # The method should return the following message:
        # "Successfully added card of type {type}Card with name: {name}"
        if type_c == 'Magic':
            self.card_repository.add(MagicCard(name))
        elif type_c == 'Trap':
            self.card_repository.add(TrapCard(name))
        return f'Successfully added card of type {type_c}Card with name: {name}'

    def add_player_card(self, username: str, card_name: str):
        # Adds the given card to the user card repository. The method should return the following message:
        # "Successfully added card: {card_name} to user: {username}"
        player = self.player_repository.find(username)
        card = self.card_repository.find(card_name)
        player.card_repository.add(card)
        return f'Successfully added card: {card_name} to user: {username}'

    def fight(self, attack_name: str, enemy_name: str):
        # The attacker and the enemy start a fight in a battlefield. The method should return the following message:
        # "Attack user health {attacker_health_left} - Enemy user health {enemy_health_left}"
        attacker = self.player_repository.find(attack_name)
        enemy = self.player_repository.find(enemy_name)

        battle_field = BattleField()
        battle_field.fight(attacker, enemy)
        return f'Attack user health {attacker.health} - Enemy user health {enemy.health}'

    def report(self):
        # Returns a report message in format:
        # Username: {username1} - Health: {health1} - Cards {cards_count1}
        # ### Card: {name1} - Damage: {card_damage1}
        result = ''

        for player in self.player_repository.players:
            result += f'Username: {player.username} - Health: {player.health} - ' \
                      f'Cards {len(player.card_repository.cards)}\n'
            for card in player.card_repository.cards:
                result += f'### Card: {card.name} - Damage: {card.damage_points}\n'
        return result
