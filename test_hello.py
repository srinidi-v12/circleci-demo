import unittest
from hello import say_hello

class TestHello(unittest.TestCase):
    def test_greeting(self):
        self.assertEqual(say_hello("CircleCI"), "Hey, CircleCI!")

if __name__ == "__main__":
    unittest.main()
