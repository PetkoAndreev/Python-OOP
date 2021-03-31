import unittest

from python_oop.testing.lab.cat import Cat


class CatTests(unittest.TestCase):
    name = 'Kitty'

    def setUp(self):
        self.cat = Cat(self.name)

    def test_cat_increase_size_after_eat(self):
        # Cat's size is increased after eating
        self.cat.eat()
        self.assertEqual(1, self.cat.size)

    def test_cat_fed_after_eat(self):
        # Cat is fed after eating
        self.cat.eat()
        self.assertTrue(self.cat.fed)

    def test_cat_cannot_eat_when_fed_exception(self):
        # Cat cannot eat if already fed, raises an error
        self.cat.eat()
        with self.assertRaises(Exception):
            self.cat.eat()

    def test_cat_cannot_asleep_when_not_fed_exception(self):
        # Cat cannot fall asleep if not fed, raises an error
        with self.assertRaises(Exception):
            self.cat.sleep()

    def test_cat_not_sleepy_when_already_sleep(self):
        # Cat is not sleepy after sleeping
        self.cat.eat()
        self.cat.sleep()
        self.assertFalse(self.cat.sleepy)


if __name__ == '__main__':
    unittest.main()
