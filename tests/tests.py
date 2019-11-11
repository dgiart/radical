import sys, os
import unittest

sys.path.append(os.getcwd())
from main import *


class TestNitrosalt(unittest.TestCase):
    def test_nitro_salt_returns_mass(self):
        self.assertEqual(nitro_salt(1000),10)
        self.assertEqual(nitro_salt(1500),15)

    def test_nitro_salt_returns_int(self):
        self.assertIsInstance(nitro_salt(1000), int)

    def test_nitro_salt_receives_str_returns_int(self):
        self.assertEqual(nitro_salt('1000'),10)

    def test_nitro_salt_receives_alpha_returns_zero(self):
        self.assertEqual(nitro_salt('sldvg'),0)


if __name__ == '__main__':
    unittest.main()
