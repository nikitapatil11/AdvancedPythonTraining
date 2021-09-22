# small class function normal --> addition,sub,mul

# simple test cases
# python -m unittest test_module test_upper
# python -m unittest testmodule.Testclass
# python -m unittest testmodule.Testclass.test_method



import unittest

class Testexample1(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('NIKITA'.upper(), "NIKITA")

    def test_isupper(self):
        self.assertTrue('NIKITA'.isupper())
        self.assertFalse('NIKITA'.isupper())

    def test_split(self):
        s = "hello world"
        self.assertEqual(s.split(), ['hello', 'world'])

if __name__ == "__main__":
    unittest.main()
