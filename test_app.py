import unittest
from main import test


class TestApp(unittest.TestCase):

    def test_test(self):
        self.assertEqual(test(), "cicd!\n")


if __name__ == '__main__':
    unittest.main()
