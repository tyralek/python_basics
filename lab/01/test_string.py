import unittest


class Test(unittest.TestCase):

    def setUp(self):
        self.a = "ala ma kota"

    def tearDown(self):
        pass

    def test_split(self):
        b = self.a
        self.assertEqual('ma', b)

    def test_range(self):
        b = self.a
        self.assertEqual('kota', b)

    def test_step(self):
        b = self.a
        self.assertEqual('aa', b)

    def test_step_revert(self):
        b = self.a
        self.assertEqual('atok am ala', b)

    def test_format(self):
        b = "{}".format(self.a)
        self.assertEqual("Czy ala ma kota, czy psa?", b)
