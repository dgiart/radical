import sys, os
import unittest

sys.path.append(os.getcwd())
from main import *


class TestNitrosalt(unittest.TestCase):
    def test_nitro_salt_returns_mass1(self):
        print (1111)
        import sys
        print (sys.version)
        self.assertEqual(nitro_salt(1000),10)
        self.assertEqual(nitro_salt(1500),15)

    def test_nitro_salt_returns_int2(self):
        print (2)
        self.assertIsInstance(nitro_salt(1000.2), int)
        # self.assertIsInstance(nitro_salt('ggkjg'), int)

    def test_nitro_salt_receives_str_returns_int3(self):
        print (3)
        self.assertEqual(nitro_salt('1000'),10)

    def test_nitro_salt_receives_alpha_returns_zero4(self):
        print (4)
        self.assertEqual(nitro_salt('sldvg'),0)


class TestSugar(unittest.TestCase):
    def test_sugar_mass5(self):

        self.assertEqual(sugar(2000),10)
        # self.assertEqual(sugar(2000),20)

if __name__ == '__main__':
    unittest.main()
