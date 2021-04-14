import unittest

from project.train.train import Train


class TrainTest(unittest.TestCase):
    name = 'Train1'
    capacity = 5
    TRAIN_FULL = "Train is full"
    PASSENGER_EXISTS = "Passenger {} Exists"
    PASSENGER_NOT_FOUND = "Passenger Not Found"
    PASSENGER_ADD = "Added passenger {}"
    PASSENGER_REMOVED = "Removed {}"
    ZERO_CAPACITY = 0

    def setUp(self):
        self.train = Train(self.name, self.capacity)

    def test_init_attr(self):
        self.assertEqual('Train1', self.train.name)
        self.assertEqual(5, self.train.capacity)
        self.assertListEqual([], self.train.passengers)
        self.assertEqual("Train is full", self.train.TRAIN_FULL)
        self.assertEqual("Passenger {} Exists", self.train.PASSENGER_EXISTS)
        self.assertEqual("Passenger Not Found", self.train.PASSENGER_NOT_FOUND)
        self.assertEqual("Added passenger {}", self.train.PASSENGER_ADD)
        self.assertEqual("Removed {}", self.train.PASSENGER_REMOVED)
        self.assertEqual(0, self.train.ZERO_CAPACITY)

    def test_add__expect_to_add_passenger(self):
        self.train.add('Pesho')

        actual = self.PASSENGER_ADD.format('Pesho')
        expect = "Added passenger Pesho"
        self.assertEqual(expect, actual)

        self.assertEqual(1, len(self.train.passengers))

    def test_add__when_train_is_full__expect_to_raise_exception(self):
        self.train.add('Pesho')
        self.train.add('Pesho1')
        self.train.add('Pesho2')
        self.train.add('Pesho3')
        self.train.add('Pesho4')
        with self.assertRaises(ValueError) as ex:
            self.train.add('Pesho5')

        actual = self.TRAIN_FULL
        expect = "Train is full"
        self.assertEqual(expect, actual)

        actual2 = str(ex.exception)
        self.assertEqual(expect, actual2)

        self.assertEqual(5, len(self.train.passengers))

    def test_add__when_passenger_exists__expect_to_raise_exception(self):
        self.train.add('Pesho')
        with self.assertRaises(ValueError) as ex:
            self.train.add('Pesho')

        actual = self.PASSENGER_EXISTS.format('Pesho')
        expect = "Passenger Pesho Exists"
        self.assertEqual(expect, actual)

        actual2 = str(ex.exception)
        self.assertEqual(expect, actual2)

        self.assertEqual(1, len(self.train.passengers))

    def test_remove__expect_to_remove_passenger(self):
        self.train.add('Pesho')
        self.assertEqual(1, len(self.train.passengers))
        self.train.remove('Pesho')

        actual = self.PASSENGER_REMOVED.format('Pesho')
        expect = "Removed Pesho"
        self.assertEqual(expect, actual)
        self.assertEqual(0, len(self.train.passengers))

    def test_remove__when_passenger_not_exists__expect_to_raise_exception(self):
        with self.assertRaises(ValueError) as ex:
            self.train.remove('Pesho')

        actual = self.PASSENGER_NOT_FOUND.format('Pesho')
        expect = "Passenger Not Found"
        self.assertEqual(expect, actual)

        actual2 = str(ex.exception)
        self.assertEqual(expect, actual2)
        self.assertEqual(0, len(self.train.passengers))


if __name__ == '__main__':
    unittest.main()
