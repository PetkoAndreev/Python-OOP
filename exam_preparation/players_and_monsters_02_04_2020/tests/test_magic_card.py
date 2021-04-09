import unittest

from project.card.magic_card import MagicCard


class TestMagicCard(unittest.TestCase):
    def setUp(self):
        self.magic_card = MagicCard('Magic')

    def test_attributes(self):
        self.assertEqual('Magic', self.magic_card.name)
        self.assertEqual(5, self.magic_card.DAMAGE_POINTS)
        self.assertEqual(80, self.magic_card.HEALTH_POINTS)

    def test_name__when_empty_string__expect_to_raise_exception(self):
        with self.assertRaises(ValueError) as context:
            self.magic_card.name = ''
        expect = "Card's name cannot be an empty string."
        actual = str(context.exception)
        self.assertEqual(expect, actual)

    def test_damage_points__when_less_than_0__expect_to_raise_exception(self):
        with self.assertRaises(ValueError) as context:
            self.magic_card.damage_points = -5
        expect = "Card's damage points cannot be less than zero."
        actual = str(context.exception)
        self.assertEqual(expect, actual)

    def test_health_points__when_less_than_0__expect_to_raise_exception(self):
        with self.assertRaises(ValueError) as context:
            self.magic_card.health_points = -5
        expect = "Card's HP cannot be less than zero."
        actual = str(context.exception)
        self.assertEqual(expect, actual)



if __name__ == '__main__':
    unittest.main()
