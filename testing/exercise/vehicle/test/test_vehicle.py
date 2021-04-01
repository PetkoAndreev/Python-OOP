import unittest

from python_oop.testing.exercise.vehicle.project.vehicle import Vehicle
# from project.vehicle import Vehicle


class VehicleTest(unittest.TestCase):
    def setUp(self):
        self.vehicle = Vehicle(50.0, 300.0)

    def test_vehicle__init_method(self):
        self.assertEqual(50.0, self.vehicle.fuel)
        self.assertEqual(50.0, self.vehicle.capacity)
        self.assertEqual(300.0, self.vehicle.horse_power)
        self.assertEqual(self.vehicle.DEFAULT_FUEL_CONSUMPTION, self.vehicle.fuel_consumption)

    def test_vehicle__fuel_capacity_if_fuel_changed(self):
        self.assertEqual(50.0, self.vehicle.capacity)
        self.vehicle.fuel = 20.0
        self.assertEqual(50.0, self.vehicle.capacity)

    def test_vehicle__str_method(self):
        expected_result = f"The vehicle has {self.vehicle.horse_power} " \
                          f"horse power with {self.vehicle.fuel} fuel left and {self.vehicle.fuel_consumption} fuel consumption"
        actual_result = self.vehicle.__str__()
        self.assertEqual(expected_result, actual_result)

    def test_vehicle__drive_method_success(self):
        self.vehicle.drive(5)
        self.assertEqual(43.75, self.vehicle.fuel)

    def test_vehicle__drive_method__expect_exception(self):
        expected_result = "Not enough fuel"
        with self.assertRaises(Exception) as context:
            self.vehicle.drive(100)
        self.assertEqual(expected_result, str(context.exception))

    def test_vehicle__refuel_method_success(self):
        self.vehicle.drive(5)
        self.vehicle.refuel(6.25)

        self.assertEqual(50.0, self.vehicle.fuel)

    def test_vehicle__refuel_method__expect_exception(self):
        expected_result = "Too much fuel"
        with self.assertRaises(Exception) as context:
            self.vehicle.refuel(100)
        self.assertEqual(expected_result, str(context.exception))


if __name__ == '__main__':
    unittest.main()
