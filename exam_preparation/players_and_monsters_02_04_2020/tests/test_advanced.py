import unittest

from project.player.advanced import Advanced


class TestBeginner(unittest.TestCase):
    def setUp(self):
        self.advanced = Advanced('Pesho')

    def test_name_and_health__expect_to_be_ok(self):
        self.assertEqual('Pesho', self.advanced.username)
        self.assertEqual(250, self.advanced.HEALTH)
        self.assertEqual('CardRepository', self.advanced.card_repository.__class__.__name__)

    def test_name__when_name_empty__expect_to_raise_exception(self):
        with self.assertRaises(ValueError) as ex:
            self.advanced.username = ''

        expect = "Player's username cannot be an empty string."
        self.assertEqual(expect, str(ex.exception))

    def test_health_when_health_less_than_0__expect_to_raise_exception(self):
        with self.assertRaises(ValueError) as ex:
            self.advanced.health = -5

        expect = "Player's health bonus cannot be less than zero."
        self.assertEqual(expect, str(ex.exception))

    def test_is_dead__when_health_greater_than_0__expect_to_be_false(self):
        self.advanced.health = 5
        self.assertFalse(False, self.advanced.is_dead)

    def test_is_dead__when_health_equal_to_0__expect_to_be_true(self):
        self.advanced.health = 0
        self.assertTrue(self.advanced.is_dead)

    def test_take_damage__expect_to_be_ok(self):
        self.advanced.take_damage(5)
        actual = self.advanced.health
        expect = 245
        self.assertEqual(expect, actual)

    def test_take_damage__when_damege_less_than_0__expect_to_raise_exception(self):
        with self.assertRaises(ValueError) as ex:
            self.advanced.take_damage(-5)
        actual = str(ex.exception)
        expect = 'Damage points cannot be less than zero.'
        self.assertEqual(expect, actual)


if __name__ == '__main__':
    unittest.main()
