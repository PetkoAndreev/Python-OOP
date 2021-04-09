import unittest

from project.player.beginner import Beginner
from project.player.player_repository import PlayerRepository


class TestPlayerRepository(unittest.TestCase):
    def setUp(self):
        self.player_repo = PlayerRepository()

    def test_attributes(self):
        self.assertEqual(0, self.player_repo.count)
        self.assertListEqual([], self.player_repo.players)

    def test_add__expect_to_add_the_card(self):
        player = Beginner('Pesho')
        self.player_repo.add(player)
        self.assertEqual(1, self.player_repo.count)
        self.assertEqual(1, len(self.player_repo.players))

    def test_add__when_card_exists__expect_to_raise_exception(self):
        player = Beginner('Pesho')
        self.player_repo.add(player)
        with self.assertRaises(ValueError) as ex:
            self.player_repo.add(player)
        expect = 'Player Pesho already exists!'
        self.assertEqual(expect, str(ex.exception))

    def test_remove__expect_to_remove_the_card(self):
        player = Beginner('Pesho')
        self.player_repo.add(player)
        self.player_repo.remove(player.username)
        self.assertEqual(0, self.player_repo.count)
        self.assertListEqual([], self.player_repo.players)

    def test_remove__when_card_is_empty_string__expect_to_raise_exception(self):
        with self.assertRaises(ValueError) as ex:
            self.player_repo.remove('')
        expect = 'Player cannot be an empty string!'
        self.assertEqual(expect, str(ex.exception))

    def test_find__expect_to_return_card(self):
        player = Beginner('Pesho')
        self.player_repo.add(player)
        actual = self.player_repo.find(player.username)
        self.assertEqual('Pesho', actual.username)


if __name__ == '__main__':
    unittest.main()