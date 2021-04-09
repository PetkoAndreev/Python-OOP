import unittest

from project.appliances.tv import TV
from project.people.child import Child
from project.rooms.room import Room


class TestRoom(unittest.TestCase):
    family_name = 'TestRoom'
    budget = 500
    members_count = 2

    def setUp(self):
        self.room = Room(self.family_name, self.budget, self.members_count)

    def test_init_attributes__expect_to_be_ok(self):
        self.assertEqual(self.family_name, self.room.family_name)
        self.assertEqual(self.budget, self.room.budget)
        self.assertEqual(self.members_count, self.room.members_count)
        self.assertListEqual([], self.room.children)
        self.assertEqual(0, self.room.expenses)

    def test_expenses__when_positive__expect_to_return_expenses(self):
        self.room.expenses = 5

        self.assertEqual(5, self.room.expenses)

    def test_expenses__when_0__expect_to_return_expenses(self):
        self.room.expenses = 0

        self.assertEqual(0, self.room.expenses)

    def test_expenses__when_negative__expect_to_raise_exception(self):
        with self.assertRaises(ValueError) as e:
            self.room.expenses = -5

        self.assertEqual('Expenses cannot be negative', str(e.exception))

    def test_calculate_expenses__when_no_aplliances__expect_to_be_0(self):
        consumers = []
        self.room.calculate_expenses(consumers)
        self.assertEqual(0, self.room.expenses)

    def test_calculate_expenses__when_one_child__expect_to_calculate_them(self):
        consumers = [Child(5, 2, 2)]
        self.room.calculate_expenses(consumers)
        self.assertEqual(consumers[0].get_monthly_expense(), self.room.expenses)

    def test_calculate_expenses__when_one_child_and_one_appliance__expect_to_calculate_them(self):
        consumers = [Child(5, 2, 2), TV()]
        self.room.calculate_expenses(consumers)
        expect = consumers[0].get_monthly_expense() + consumers[1].get_monthly_expense()
        self.assertEqual(expect, self.room.expenses)


if __name__ == '__main__':
    unittest.main()
