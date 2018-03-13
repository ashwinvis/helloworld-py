import unittest
from HelloWorld import func_hello


class TestHello(unittest.TestCase):
    def test_hello(self):
        assert func_hello.hello() == 'hello'


if __name__ == '__main__':
    unittest.main()
