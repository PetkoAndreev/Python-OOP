import unittest

from project.card.card_repository import CardRepository
from project.card.magic_card import MagicCard


class TestCardRepository(unittest.TestCase):
    def setUp(self):
        self.card_repo = CardRepository()

    def test_attributes(self):
        self.assertEqual(0, self.card_repo.count)
        self.assertListEqual([], self.card_repo.cards)

    def test_add__expect_to_add_the_card(self):
        card = MagicCard('Fire')
        self.card_repo.add(card)
        self.assertEqual(1, self.card_repo.count)
        self.assertEqual(1, len(self.card_repo.cards))

    def test_add__when_card_exists__expect_to_raise_exception(self):
        card = MagicCard('Fire')
        self.card_repo.add(card)
        with self.assertRaises(ValueError) as ex:
            self.card_repo.add(card)
        expect = 'Card Fire already exists!'
        self.assertEqual(expect, str(ex.exception))

    def test_remove__expect_to_remove_the_card(self):
        card = MagicCard('Fire')
        self.card_repo.add(card)
        self.card_repo.remove(card.name)
        self.assertEqual(0, self.card_repo.count)
        self.assertListEqual([], self.card_repo.cards)

    def test_remove__when_card_is_empty_string__expect_to_raise_exception(self):
        with self.assertRaises(ValueError) as ex:
            self.card_repo.remove('')
        expect = 'Card cannot be an empty string!'
        self.assertEqual(expect, str(ex.exception))

    def test_find__expect_to_return_card(self):
        card = MagicCard('Fire')
        self.card_repo.add(card)
        actual = self.card_repo.find(card.name)
        self.assertEqual('Fire', actual.name)


if __name__ == '__main__':
    unittest.main()