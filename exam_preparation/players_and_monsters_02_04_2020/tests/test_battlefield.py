import unittest

from project.battle_field import BattleField
from project.card.magic_card import MagicCard
from project.card.trap_card import TrapCard
from project.player.advanced import Advanced
from project.player.beginner import Beginner


class TestBattleField(unittest.TestCase):
    def setUp(self):
        self.battle_field = BattleField()

    def test_fight__when_attacker_is_dead__expect_to_raise_exception(self):
        attacker = Beginner('Pesho')
        enemy = Beginner('Gosho')
        attacker.health = 0

        with self.assertRaises(ValueError) as context:
            self.battle_field.fight(attacker, enemy)
        expect = 'Player is dead!'
        actual = str(context.exception)

        self.assertEqual(expect, actual)

    def test_fight__when_enemy_is_dead__expect_to_raise_exception(self):
        attacker = Beginner('Pesho')
        enemy = Beginner('Gosho')
        enemy.health = 0

        with self.assertRaises(ValueError) as context:
            self.battle_field.fight(attacker, enemy)
        expect = 'Player is dead!'
        actual = str(context.exception)

        self.assertEqual(expect, actual)

    def test_fight__when_attacker_is_beginner_without_cards__expect_to_increase_health(self):
        attacker = Beginner('Pesho')
        enemy = Advanced('Gosho')
        self.battle_field.fight(attacker, enemy)

        self.assertEqual(50 + 40, attacker.health)
        self.assertEqual(250, enemy.health)

    def test_fight__when_enemy_is_beginner_without_cards__expect_to_increase_health(self):
        attacker = Advanced('Pesho')
        enemy = Beginner('Gosho')
        self.battle_field.fight(attacker, enemy)

        self.assertEqual(50 + 40, enemy.health)
        self.assertEqual(250, attacker.health)

    def test_fight__when_attacker_is_beginner_with_cards__expect_to_increase_health(self):
        attacker = Beginner('Pesho')
        enemy = Advanced('Gosho')
        card1 = MagicCard('Monster Reborn')
        card2 = TrapCard('Dark Hole')
        attacker.card_repository.add(card1)
        attacker.card_repository.add(card2)
        self.battle_field.fight(attacker, enemy)

        self.assertEqual(50 + 40 + card1.HEALTH_POINTS + card2.HEALTH_POINTS, attacker.health)

    def test_fight__when_enemy_is_advanced_with_cards__expect_to_increase_health(self):
        attacker = Advanced('Pesho')
        enemy = Beginner('Gosho')
        card1 = MagicCard('Monster Reborn')
        card2 = TrapCard('Dark Hole')
        enemy.card_repository.add(card1)
        enemy.card_repository.add(card2)
        self.battle_field.fight(attacker, enemy)

        self.assertEqual(50 + 40 + card1.HEALTH_POINTS + card2.HEALTH_POINTS, enemy.health)

if __name__ == '__main__':
    unittest.main()
