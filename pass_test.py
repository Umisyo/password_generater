import unittest
import re
from main import PassWord

class PasswordTest(unittest.TestCase):
    def setUp(self):
        self.pw = PassWord(8)

    def tearDown(self):
        pass

    def test_length(self):
        for i in range(1, 10):
            pw = PassWord(i)
            self.assertEqual(i, len(pw.pass_word))

    def test_match(self):
        pw = PassWord(8)
        pattern = '(?=.*[a-z]+)(?=.*[A-Z]+)(?=.*[0-9]+)(?=.*[!"#$%&\-^¥\\@;:\/<>\+\*{}\[\]\|~=]).*$'
        m = re.match(pattern, self.pw.pass_word)

        self.assertEqual(m.group(0), self.pw.pass_word)

    if __name__ == '__main__':
        unittest.main()

