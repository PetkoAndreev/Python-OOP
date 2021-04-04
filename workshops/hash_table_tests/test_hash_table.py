import unittest

from python_oop.workshops.hash_table.hashtable import HashTable


class TestHashTable(unittest.TestCase):
    def setUp(self):
        self.hash_table = HashTable()

    def test_attributes(self):
        self.assertEqual(4, len(self.hash_table.keys))
        self.assertEqual(4, len(self.hash_table.values))
        self.assertEqual(4, self.hash_table.max_capacity)

    def test_add_with_available_space(self):
        self.hash_table.add("Test_key1", "Value1")
        self.assertEqual(1, self.hash_table.actual_length)
        self.assertEqual(4, self.hash_table.max_capacity)
        self.assertEqual("Value1", self.hash_table["Test_key1"])

    def test_add_with_no_available_space_resizes(self):
        for num in range(1, self.hash_table.max_capacity + 1):
            self.hash_table.add(f"Test_key{num}", f"Value{num}")
        self.assertEqual(4, self.hash_table.actual_length)
        self.assertEqual(4, self.hash_table.max_capacity)

        # Overload the dict and it should resize
        self.hash_table.add("Test_key5", "Value5")
        self.assertEqual(5, self.hash_table.actual_length)
        self.assertEqual(8, self.hash_table.max_capacity)
        self.assertIn("Test_key5", self.hash_table.keys)

    def test_value_is_replaced_when_key_exists(self):
        self.hash_table.add("Test_key", "Value")
        self.assertEqual("Value", self.hash_table["Test_key"])
        self.hash_table["Test_key"] = "New_value"
        self.assertEqual("New_value", self.hash_table["Test_key"])

    def test_get_with_existing_key(self):
        self.hash_table.add("Test_key", "Value")
        self.assertEqual("Value", self.hash_table.get("Test_key"))

    def test_get_with_not_existing_key(self):
        self.hash_table.add("Test_key", "Value")
        self.assertIsNone(self.hash_table.get("not existing key"))

    def test_get_with_not_existing_key_with_default_value(self):
        self.hash_table.add("Test_key", "Value")
        self.assertEqual("DEFAULT", self.hash_table.get("not existing key", "DEFAULT"))

    def test_representation(self):
        self.hash_table.add("Test_key", "Value")
        self.assertEqual("{Test_key: Value}", str(self.hash_table))

    def test_collision_set_next_available_index(self):
        self.hash_table["name"] = "Peter"
        self.assertEqual(1, self.hash_table.keys.index("name"))
        # collision with index 1
        self.hash_table["age"] = 25
        self.assertEqual(2, self.hash_table.keys.index("age"))

    def test_collision_set_next_available_index_at_0(self):
        self.hash_table["name"] = "Peter"
        self.assertEqual(1, self.hash_table.keys.index("name"))
        # collision with index 1
        self.hash_table["age"] = 25
        self.assertEqual(2, self.hash_table.keys.index("age"))
        self.hash_table["work"] = "Some title"
        self.assertEqual(3, self.hash_table.keys.index("work"))
        # Go back to index 0, because no other available
        self.hash_table["eyes color"] = "blue"
        self.assertEqual(0, self.hash_table.keys.index("eyes color"))