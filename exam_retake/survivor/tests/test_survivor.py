import unittest

from project.survivor import Survivor


class TrainTest(unittest.TestCase):
    name = 'Pesho'
    age = 27
    health = 100
    needs = 100

    def setUp(self):
        self.survivor = Survivor(self.name, self.age)

    def test_init_attributes(self):
        self.assertEqual('Pesho', self.survivor.name)
        self.assertEqual(27, self.survivor.age)
        self.assertEqual(100, self.survivor.health)
        self.assertEqual(100, self.survivor.needs)

    def test_name__when_invalid__expect_to_raise_exception(self):
        with self.assertRaises(ValueError) as ex:
            self.survivor.name = ''
        expect = "Name not valid!"
        actual = str(ex.exception)
        self.assertEqual(expect, actual)

    def test_age__when_less_than_0__expect_to_raise_exception(self):
        with self.assertRaises(ValueError) as ex:
            self.survivor.age = -1
        expect = "Age not valid!"
        actual = str(ex.exception)
        self.assertEqual(expect, actual)

    def test_health__when_less_than_0__expect_to_raise_exception(self):
        with self.assertRaises(ValueError) as ex:
            self.survivor.health = -1
        expect = "Health not valid!"
        actual = str(ex.exception)
        self.assertEqual(expect, actual)

    def test_health__when_more_than_100__expect_to_return_100(self):
        self.survivor.health = 150
        expect = 100
        actual = self.survivor.health
        self.assertEqual(expect, actual)

    def test_needs__when_less_than_0__expect_to_raise_exception(self):
        with self.assertRaises(ValueError) as ex:
            self.survivor.needs = -1
        expect = "Needs not valid!"
        actual = str(ex.exception)
        self.assertEqual(expect, actual)

    def test_needs__when_more_than_100__expect_to_return_100(self):
        self.survivor.needs = 150
        expect = 100
        actual = self.survivor.needs
        self.assertEqual(expect, actual)

    def test_needs_sustenance__when_needs_less_than_100__expect_to_be_true(self):
        self.survivor.needs = 99
        self.assertTrue(self.survivor.needs_sustenance)

    def test_needs_sustenance__when_needs_100__expect_to_be_false(self):
        self.survivor.needs = 100
        self.assertFalse(self.survivor.needs_sustenance)

    def test_needs_healing__when_needs_less_than_100__expect_to_be_true(self):
        self.survivor.health = 99
        self.assertTrue(self.survivor.needs_healing)

    def test_needs_healing__when_needs_100__expect_to_be_false(self):
        self.survivor.health = 100
        self.assertFalse(self.survivor.needs_healing)
