import unittest
from app import test

class TestHelloApp(unittest.TestCase):

  def test_test(self):
    self.assertEqual(test(), "synopsys\n")

if __name__ == '__main__':
  unittest.main()






