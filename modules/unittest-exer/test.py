import unittest
import random
import script


class TestCase(unittest.TestCase):
    def test_random_numbers(self):
        number = input("Please enter an number: ")
        answer = random.randint(0, 10)
        self.assertEqual(number, answer)


if __name__ == "__main__":
    unittest.main()

