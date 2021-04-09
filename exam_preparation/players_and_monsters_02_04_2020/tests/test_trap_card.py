import unittest

from project.card.trap_card import TrapCard


class TestTrapcCard(unittest.TestCase):
    def setUp(self):
        self.trap_card = TrapCard('Trap')

    def test_attributes(self):
        self.assertEqual('Trap', self.trap_card.name)
        self.assertEqual(120, self.trap_card.DAMAGE_POINTS)
        self.assertEqual(5, self.trap_card.HEALTH_POINTS)

    def test_name__when_empty_string__expect_to_raise_exception(self):
        with self.assertRaises(ValueError) as context:
            self.trap_card.name = ''
        expect = "Card's name cannot be an empty string."
        actual = str(context.exception)
        self.assertEqual(expect, actual)

    def test_damage_points__when_less_than_0__expect_to_raise_exception(self):
        with self.assertRaises(ValueError) as context:
            self.trap_card.damage_points = -5
        expect = "Card's damage points cannot be less than zero."
        actual = str(context.exception)
        self.assertEqual(expect, actual)

    def test_health_points__when_less_than_0__expect_to_raise_exception(self):
        with self.assertRaises(ValueError) as context:
            self.trap_card.health_points = -5
        expect = "Card's HP cannot be less than zero."
        actual = str(context.exception)
        self.assertEqual(expect, actual)


if __name__ == '__main__':
    unittest.main()
