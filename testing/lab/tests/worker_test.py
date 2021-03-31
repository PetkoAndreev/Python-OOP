import unittest

from python_oop.testing.lab.worker import Worker


class WorkerTests(unittest.TestCase):
    name = 'Worker'
    salary = 1000
    energy = 10

    def setUp(self):
        self.worker = Worker(self.name, self.salary, self.energy)

    def test_worker_correct_initialize(self):
        # Test if the worker is initialized with correct name, salary and energy
        self.assertEqual(self.name, self.worker.name)
        self.assertEqual(self.salary, self.worker.salary)
        self.assertEqual(self.energy, self.worker.energy)

    def test_worker_energy_increment_after_rest(self):
        # Test if the worker's energy is incremented after the rest method is called
        self.worker.rest()
        self.assertEqual(self.energy + 1, self.worker.energy)

    def test_worker_try_to_work_with_0_energy_exception(self):
        # Test if an error is raised if the worker tries to work with negative energy or equal to 0
        self.worker.energy = 0
        with self.assertRaises(Exception):
            self.worker.work()

    def test_worker_correct_increase_money_by_salary_after_work_method(self):
        # Test if the worker's money is increased by his salary correctly after the work method is called
        self.worker.work()
        self.worker.work()
        self.assertEqual(self.salary * 2, self.worker.money)

    def test_worker_energy_decrease_by_work(self):
        # Test if the worker's energy is decreased after the work method is called
        self.worker.work()
        self.assertEqual(self.energy - 1, self.worker.energy)

    def test_worker_get_info_returns_proper_result(self):
        # Test if the get_info method returns the proper string with correct values
        # self.worker.get_info()
        self.assertEqual(f'{self.name} has saved 0 money.', self.worker.get_info())


if __name__ == '__main__':
    unittest.main()
