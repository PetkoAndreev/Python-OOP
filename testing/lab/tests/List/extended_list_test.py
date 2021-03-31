import unittest

from python_oop.testing.lab.List.extended_list import IntegerList


class IntegerListTest(unittest.TestCase):

    def test_integers_add_when_integer(self):
        integer_list = IntegerList()
        internal_list = integer_list.add(1)
        self.assertEqual([1], internal_list)

    def test_integers_add_when_not_integer_exception(self):
        integer_list = IntegerList()
        # internal_list = integer_list.add(1.0)
        with self.assertRaises(ValueError):
            # integer_list.add(1.0)
            integer_list.add("asd")

    def test_integers_remove_index_when_index_in_range(self):
        value_to_remove = 3
        integer_list = IntegerList(1, 2, value_to_remove, 4)

        result = integer_list.remove_index(2)
        self.assertEqual(value_to_remove, result)
        self.assertListEqual([1, 2, 4], integer_list.get_data())

    # def test_integers_remove_index_when_index_is_negative_not_in_range(self):
    #     integer_list = IntegerList(1, 2, 3, 4)
    #     index = -5
    #     with self.assertRaises(IndexError):
    #         integer_list.remove_index(index)

    def test_integers_remove_index_when_index_is_positive_not_in_range(self):
        integer_list = IntegerList(1, 2, 3, 4)
        index = 5
        with self.assertRaises(IndexError):
            integer_list.remove_index(index)

    def test_integers_init_store_only_integers(self):
        integer_list = IntegerList(1, 2, 3, 4, 'as', 1.0, 5)
        integer_list.get_data()

    def test_integers_get_when_index_in_range(self):
        value_to_get = 3
        integer_list = IntegerList(1, 2, value_to_get, 4)

        result = integer_list.get(2)
        self.assertEqual(value_to_get, result)
        self.assertListEqual([1, 2, 3, 4], integer_list.get_data())

    def test_integers_get_when_index_is_negative_not_in_range(self):
        integer_list = IntegerList(1, 2, 3, 4)
        index = -5
        with self.assertRaises(IndexError):
            integer_list.get(index)

    def test_integers_get_when_index_is_positive_not_in_range(self):
        integer_list = IntegerList(1, 2, 3, 4)
        index = 5
        with self.assertRaises(IndexError):
            integer_list.get(index)

    def test_integers_insert_when_index_in_range(self):
        value_to_insert = 3
        index_to_insert = 2
        integer_list = IntegerList(1, 2, 4)
        integer_list.insert(index_to_insert, value_to_insert)
        self.assertListEqual([1, 2, 3, 4], integer_list.get_data())

    # def test_integers_insert_when_index_is_negative_not_in_range(self):
    #     value_to_insert = 3
    #     index_to_insert = -5
    #     type(value_to_insert)
    #     integer_list = IntegerList(1, 2, 4)
    #     with self.assertRaises(IndexError):
    #         integer_list.insert(index_to_insert, value_to_insert)

    def test_integers_insert_when_index_is_positive_not_in_range(self):
        value_to_insert = 3
        index_to_insert = 5
        integer_list = IntegerList(1, 2, 4)
        with self.assertRaises(IndexError):
            integer_list.insert(index_to_insert, value_to_insert)

    def test_integers_insert_when_not_integer_exception(self):
        value_to_insert = 'asd'
        index_to_insert = 2
        integer_list = IntegerList(1, 2, 4)
        with self.assertRaises(ValueError):
            integer_list.insert(index_to_insert, value_to_insert)

    def test_integers_biggest(self):
        biggest = 17
        integer_list = IntegerList(1, 2, biggest, 4)
        self.assertEqual(biggest, integer_list.get_biggest())

    def test_integers_get_index(self):
        el = 5
        index = 4
        integer_list = IntegerList(1, 2, 3, 4, 5, 6)
        self.assertEqual(index, integer_list.get_index(el))


if __name__ == '__main__':
    unittest.main()
