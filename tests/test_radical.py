import sys, os
import unittest

sys.path.append(os.getcwd())
from radical import *
class TestRadical(unittest.TestCase):
    def test_prime_factorization(self):
        self.assertEqual(prime_factorization(600),{2:3,3:1,5:2})

    def test_mult(self):

        n=1
        d=prime_factorization(600)
        for k in d:
            n=n*k**d[k]
        self.assertEqual(n,600)
    def test_radical(self):
        self.assertEqual(radical(600),30)



if __name__ == '__main__':
    unittest.main()
