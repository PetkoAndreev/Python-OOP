from project.player.beginner import Beginner
from project.player.player import Player


class BattleField:
    @staticmethod
    def increase_health(player: Beginner):
        player.health += 40

    @staticmethod
    def increase_health_with_card_damage(player: Beginner):
        for card in player.card_repository.cards:
            card.damage_points += 30

    @staticmethod
    def get_bonus_health_points(player):
        return sum([c.health_points for c in player.card_repository.cards])

    def fight(self, attacker: Player, enemy: Player):
        # That's the most interesting method.
        # •	If one of the users is_dead, raise new ValueError with message "Player is dead!"
        # •	If a player is a beginner, increase his health with 40 points and
        #   increase the damage points of each card in the players' deck with 30.
        # •	Before the fight, both players get bonus health points from their deck.
        #   (sum of all health points of his cards)
        # •	Attacker attacks first and after that the enemy attacks
        #   (deal damage points to opponent for each card). If one of the players is dead, you should stop the fight.
        if attacker.is_dead or enemy.is_dead:
            raise ValueError('Player is dead!')

        if isinstance(attacker, Beginner):
            self.increase_health(attacker)
            self.increase_health_with_card_damage(attacker)

        if isinstance(enemy, Beginner):
            self.increase_health(enemy)
            self.increase_health_with_card_damage(enemy)

        attacker.health += self.get_bonus_health_points(attacker)
        enemy.health += self.get_bonus_health_points(enemy)

        for card in attacker.card_repository.cards:
            if enemy.is_dead:
                return
            enemy.take_damage(card.damage_points)

        for card in enemy.card_repository.cards:
            if attacker.is_dead:
                return
            attacker.take_damage(card.damage_points)
