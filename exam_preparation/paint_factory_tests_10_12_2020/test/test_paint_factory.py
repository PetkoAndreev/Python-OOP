import unittest

from project.factory.paint_factory import PaintFactory


class TestPaintFactory(unittest.TestCase):
    name = 'Art Factory'
    capacity = 10
    valid_ingredients = ["white", "yellow", "blue", "green", "red"]
    ingredients = {}

    def setUp(self):
        self.paint_factory = PaintFactory(self.name, self.capacity)

    def test_init_attributes(self):
        self.assertEqual('Art Factory', self.paint_factory.name)
        self.assertEqual(10, self.paint_factory.capacity)
        self.assertDictEqual({}, self.paint_factory.ingredients)
        self.assertDictEqual({}, self.paint_factory.products)
        expect = ["white", "yellow", "blue", "green", "red"]
        self.assertListEqual(expect, self.paint_factory.valid_ingredients)

    def test_add_ingredient__when_ingredient_not_in_ingredients__expect_to_add(self):
        self.paint_factory.add_ingredient('white', 5)
        self.assertDictEqual({'white': 5}, self.paint_factory.ingredients)

    def test_add_ingredient__when_ingredient_in_ingredients__expect_to_increase_quantity(self):
        self.paint_factory.add_ingredient('white', 5)
        self.assertDictEqual({'white': 5}, self.paint_factory.ingredients)
        self.paint_factory.add_ingredient('white', 5)
        self.assertDictEqual({'white': 10}, self.paint_factory.ingredients)

    def test_add_ingredient__when_ingredient_type_not_in_valid_ingredient_types__expect_to_raise(self):
        with self.assertRaises(TypeError) as ex:
            self.paint_factory.add_ingredient('pink', 5)
        expect = f"Ingredient of type pink not allowed in PaintFactory"
        actual = str(ex.exception)
        self.assertEqual(expect, actual)

    def test_add_ingredient__when_ingredient_is_valid_and_capacity_is_less_than_quantity__expect_to_raise(self):
        with self.assertRaises(ValueError) as ex:
            self.paint_factory.add_ingredient('white', 15)
        expect = "Not enough space in factory"
        actual = str(ex.exception)
        self.assertEqual(expect, actual)

    def test_remove_ingredient__when_ingredient_in_ingredients__expect_to_decrease_quantity(self):
        self.paint_factory.add_ingredient('white', 5)
        self.paint_factory.remove_ingredient('white', 3)
        self.assertDictEqual({'white': 2}, self.paint_factory.ingredients)
        self.paint_factory.remove_ingredient('white', 2)
        self.assertDictEqual({'white': 0}, self.paint_factory.ingredients)

    def test_remove_ingredient__when_ingredient_not_in_ingredients__expect_to_raise_exception(self):
        with self.assertRaises(KeyError) as ex:
            self.paint_factory.remove_ingredient('pink', 5)
        expect = "No such ingredient in the factory" # Correct in Judge - Wrong in skeleton
        # expect = "No such product in the factory" # Wrong in Judge - Correct in skeleton
        actual = str(ex.exception.args[0])
        self.assertEqual(expect, actual)

    def test_remove_ingredient__when_ingredient_quantity_is_big_than_stored_quantity__expect_to_raise_exception(self):
        self.paint_factory.add_ingredient('white', 10)
        with self.assertRaises(ValueError) as ex:
            self.paint_factory.remove_ingredient('white', 25)
        expect = "Ingredient quantity cannot be less than zero"
        actual = str(ex.exception)
        self.assertEqual(expect, actual)

    def test_product_property__expect_to_return_ingredients(self):
        self.assertDictEqual({}, self.paint_factory.products)
        self.paint_factory.add_ingredient('white', 10)
        self.assertDictEqual({'white': 10}, self.paint_factory.products)

    def test_can_add__expect_to_return_true(self):
        self.assertTrue(self.paint_factory.can_add(10))

    def test_can_add__expect_to_return_false(self):
        self.assertFalse(self.paint_factory.can_add(11))


if __name__ == '__main__':
    unittest.main()
