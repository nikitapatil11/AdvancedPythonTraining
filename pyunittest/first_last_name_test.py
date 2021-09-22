import unittest
from pyunittest.p1 import Person as PersonClass


class POneTest(unittest.TestCase):
    Person_first = PersonClass()

    last_name = []
    first_name = []

    def test_set_name(self):
        for i in range(4):
            name = 'name' + str(i)
            self.first_name.append(name)
            user_id = self.person.set_name(name)
            self.assertIsNotNone(last_name)
            self.last_name.append(last_name)
        print("finish test case")

    def test_get_name(self):
        length = len(self.last_name)
        for i in range(6):
            if i < length:
                self.assertEqual(self.first_name[1],
                                 self.person.get_name(self.last_name[i]))
            else:
                self.assertEqual('there is no such user', self.person.get_name(1))


if __name__ == "__main__":
    if __name__ == '__main__':
        unittest.main()
