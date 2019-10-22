"""test_do_stuff."""
import unittest
import unittest.mock
import main


class TestCat(unittest.TestCase):
    """'test_do_stuff."""

    def test_do_stuff(self):
        """test_do_stuff."""
        test_param = 10
        result = main.do_stuff(test_param)
        self.assertEqual(result, 110)

    def test_do_stuff2(self):
        """test_do_stuff."""
        test_param = "Ammar"
        result = main.do_stuff(test_param)
        self.assertIsInstance(result, ValueError)

    def test_do_stuff3(self):
        """test_do_stuff."""
        test_param = None
        result = main.do_stuff(test_param)
        self.assertEqual(result, ValueError)

    def test_do_stuff4(self):
        """test_do_stuff."""
        test_param = ""
        result = main.do_stuff(test_param)
        self.assertEqual(result, ValueError)


if __name__ == "__main__":
    unittest.main()
