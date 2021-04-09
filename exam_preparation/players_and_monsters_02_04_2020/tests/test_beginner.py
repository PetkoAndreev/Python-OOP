import unittest

from project.player.beginner import Beginner


class TestBeginner(unittest.TestCase):
    def setUp(self):
        self.beginner = Beginner('Pesho')

    def test_name_and_health__expect_to_be_ok(self):
        self.assertEqual('Pesho', self.beginner.username)
        self.assertEqual(50, self.beginner.HEALTH)
        self.assertEqual('CardRepository', self.beginner.card_repository.__class__.__name__)

    def test_name__when_name_empty__expect_to_raise_exception(self):
        with self.assertRaises(ValueError) as ex:
            self.beginner.username = ''

        expect = "Player's username cannot be an empty string."
        self.assertEqual(expect, str(ex.exception))

    def test_health_when_health_less_than_0__expect_to_raise_exception(self):
        with self.assertRaises(ValueError) as ex:
            self.beginner.health = -5

        expect = "Player's health bonus cannot be less than zero."
        self.assertEqual(expect, str(ex.exception))

    def test_is_dead__when_health_greater_than_0__expect_to_be_false(self):
        self.beginner.health = 5
        self.assertFalse(False, self.beginner.is_dead)

    def test_is_dead__when_health_equal_to_0__expect_to_be_true(self):
        self.beginner.health = 0
        self.assertTrue(self.beginner.is_dead)

    def test_take_damage__expect_to_be_ok(self):
        self.beginner.take_damage(5)
        actual = self.beginner.health
        expect = 45
        self.assertEqual(expect, actual)

    def test_take_damage__when_damege_less_than_0__expect_to_raise_exception(self):
        with self.assertRaises(ValueError) as ex:
            self.beginner.take_damage(-5)
        actual = str(ex.exception)
        expect = 'Damage points cannot be less than zero.'
        self.assertEqual(expect, actual)


if __name__ == '__main__':
    unittest.main()
