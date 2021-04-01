import unittest


from python_oop.testing.exercise.mammal.project.mammal import Mammal
# from project.mammal import Mammal


class MammalTest(unittest.TestCase):
    name = 'Cow'
    type = 'Mammal'
    sound = 'Muuu'

    def test_mammal_name(self):
        mammal = Mammal(self.name, self.type, self.sound)
        expected_name = 'Cow'
        self.assertEqual(expected_name, mammal.name)

    def test_mammal_type(self):
        mammal = Mammal(self.name, self.type, self.sound)
        expected_type = 'Mammal'
        self.assertEqual(expected_type, mammal.type)

    def test_mammal_sound(self):
        mammal = Mammal(self.name, self.type, self.sound)
        expected_sound = 'Muuu'
        self.assertEqual(expected_sound, mammal.sound)

    def test_mammal_kingdom_initial(self):
        mammal = Mammal(self.name, self.type, self.sound)
        result = mammal._Mammal__kingdom
        expected_result = "animals"
        self.assertEqual(result, expected_result)

    def test_mammal_make_sound(self):
        mammal = Mammal(self.name, self.type, self.sound)

        self.assertEqual(f"{self.name} makes {self.sound}", mammal.make_sound())

    def test_mammal_info(self):
        mammal = Mammal(self.name, self.type, self.sound)

        self.assertEqual(f"{self.name} is of type {self.type}", mammal.info())

    def test_mammal_get_kingdom(self):
        mammal = Mammal(self.name, self.type, self.sound)
        result = mammal.get_kingdom()
        expected_result = 'animals'
        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    unittest.main()
