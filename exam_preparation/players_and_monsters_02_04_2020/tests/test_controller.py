import unittest

from project.battle_field import BattleField
from project.controller import Controller
from project.player.beginner import Beginner


class TestController(unittest.TestCase):
    def setUp(self):
        self.controller = Controller()

    def test_attributes(self):
        self.assertEqual('PlayerRepository', self.controller.player_repository.__class__.__name__)
        self.assertEqual('CardRepository', self.controller.card_repository.__class__.__name__)

    def test_add_player__when_player_is_beginner__expect_to_add_it(self):
        type_p = 'Beginner'
        username = 'Pesho'
        expect = 'Successfully added player of type Beginner with username: Pesho'
        self.assertEqual(expect, self.controller.add_player(type_p, username))
        self.assertEqual(1, len(self.controller.player_repository.players))

    def test_add_player__when_player_is_advanced__expect_to_add_it(self):
        type_p = 'Advanced'
        username = 'Gosho'
        expect = 'Successfully added player of type Advanced with username: Gosho'
        self.assertEqual(expect, self.controller.add_player(type_p, username))
        self.assertEqual(1, len(self.controller.player_repository.players))

    def test_add_card__when_card_is_trap__expect_to_add_it(self):
        type_c = 'Trap'
        name = 'Dark Hole'
        expect = 'Successfully added card of type TrapCard with name: Dark Hole'
        self.assertEqual(expect, self.controller.add_card(type_c, name))
        self.assertEqual(1, len(self.controller.card_repository.cards))

    def test_add_card__when_card_is_magic__expect_to_add_it(self):
        type_c = 'Magic'
        name = 'Monster reborn'
        expect = 'Successfully added card of type MagicCard with name: Monster reborn'
        self.assertEqual(expect, self.controller.add_card(type_c, name))
        self.assertEqual(1, len(self.controller.card_repository.cards))

    def test_add_player_card__expect_to_add_it(self):
        username = 'Pesho'
        self.controller.add_player('Advanced', username)
        card_name = 'Monster reborn'
        self.controller.add_card('Magic', card_name)

        player = self.controller.player_repository.find(username)
        card = self.controller.card_repository.find(card_name)
        expect = 'Successfully added card: Monster reborn to user: Pesho'
        self.assertEqual(expect, self.controller.add_player_card(username, card_name))
        self.assertEqual(1, len(player.card_repository.cards))

    def test_fight__expect_to_return_attacker_and_enemy_healths(self):
        attack_name = 'Pesho'
        self.controller.add_player('Advanced', attack_name)
        enemy_name = 'Gosho'
        self.controller.add_player('Advanced', enemy_name)
        actual = self.controller.fight(attack_name, enemy_name)
        expect = 'Attack user health 250 - Enemy user health 250'
        self.assertEqual(expect, actual)

    def test_report__expect_to_return_it(self):
        type_p = 'Beginner'
        username = 'Pesho'
        self.controller.add_player(type_p, username)
        type_c = 'Trap'
        name = 'Dark Hole'
        self.controller.add_card(type_c, name)
        self.controller.add_player_card(username, name)
        type_c = 'Magic'
        name = 'Monster reborn'
        self.controller.add_card(type_c, name)
        self.controller.add_player_card(username, name)

        expect = 'Username: Pesho - Health: 50 - ' \
                 'Cards 2\n' \
                 '### Card: Dark Hole - Damage: 120\n' \
                 '### Card: Monster reborn - Damage: 5\n'
        actual = self.controller.report()

        self.assertEqual(expect, actual)


if __name__ == '__main__':
    unittest.main()
