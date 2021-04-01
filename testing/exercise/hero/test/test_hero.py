import unittest

# from python_oop.testing.exercise.hero.project.hero import Hero
from project.hero import Hero


class HeroTest(unittest.TestCase):
    def setUp(self):
        self.hero = Hero('Blue Mage', 10, 1000.1, 100.2)

    def test_hero_init_method_attributes(self):
        self.assertEqual('Blue Mage', self.hero.username)
        self.assertEqual(10, self.hero.level)
        self.assertEqual(1000.1, self.hero.health)
        self.assertEqual(100.2, self.hero.damage)

    def test_hero_str_method(self):
        expected_result = f"Hero Blue Mage: 10 lvl\nHealth: 1000.1\nDamage: 100.2\n"
        actual_result = self.hero.__str__()
        self.assertEqual(expected_result, actual_result)

    def test_hero_battle_when_enemy_hero_name_same_as_hero_name(self):
        enemy_hero = self.hero
        with self.assertRaises(Exception) as context:
            self.hero.battle(enemy_hero)
        self.assertEqual("You cannot fight yourself", str(context.exception))

    def test_hero_battle_when_hero_health_is_0(self):
        enemy_hero = Hero('Hero', 5, 100, 3)
        self.hero.health = 0
        with self.assertRaises(ValueError) as context:
            self.hero.battle(enemy_hero)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(context.exception))

    def test_hero_battle_when_hero_health_is_less_than_0(self):
        enemy_hero = Hero('Hero', 5, 100, 3)
        self.hero.health = -5
        with self.assertRaises(ValueError) as context:
            self.hero.battle(enemy_hero)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(context.exception))

    def test_hero_battle_when_enemy_hero_health_is_0(self):
        enemy_hero = Hero('Knight', 5, 0, 3)
        with self.assertRaises(ValueError) as context:
            self.hero.battle(enemy_hero)
        self.assertEqual("You cannot fight Knight. He needs to rest", str(context.exception))

    def test_hero_battle_when_enemy_hero_health_is_less_than_0(self):
        enemy_hero = Hero('Knight', 5, -100, 3)
        with self.assertRaises(ValueError) as context:
            self.hero.battle(enemy_hero)
        self.assertEqual("You cannot fight Knight. He needs to rest", str(context.exception))

    def test_hero_battle_when_battle_is_draw(self):
        enemy_hero = Hero('Knight', 10, 1000.1, 100.2)
        expected_result = "Draw"
        actual_result = self.hero.battle(enemy_hero)
        self.assertEqual(expected_result, actual_result)

    def test_hero_battle_when_hero_wins(self):
        enemy_hero = Hero('Knight', 5, 100, 3)
        expected_result = "You win"
        actual_result = self.hero.battle(enemy_hero)
        self.assertEqual(expected_result, actual_result)
        self.assertEqual(11, self.hero.level)
        self.assertEqual(990.1, self.hero.health)
        self.assertEqual(105.2, self.hero.damage)

    def test_hero_battle_when_enemy_hero_wins(self):
        enemy_hero = Hero('Knight', 11, 10000, 110)
        expected_result = "You lose"
        actual_result = self.hero.battle(enemy_hero)
        self.assertEqual(expected_result, actual_result)
        self.assertEqual(12, enemy_hero.level)
        self.assertEqual(9003, enemy_hero.health)
        self.assertEqual(115, enemy_hero.damage)


if __name__ == '__main__':
    unittest.main()
