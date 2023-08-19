import unittest
import cplx_lib

class Test_cplx_functions(unittest.TestCase):

    def test_suma(self):
        # (3 + 2i) + (-5 + 5.2i) = (-2, 7.2i)
        c1 = (3,2)
        c2 = (-5,5.2)
        self.assertAlmostEqual(cplx_lib.suma_cplx(c1,c2),(-2,7.2))
        # (3 + 5i) + (-2.6 + 6.8i) = (0.4, 11.8i)
        suma = cplx_lib.suma_cplx((3,5),(-2.6,6.8))
        self.assertAlmostEqual(suma[0], 0.4)
        self.assertAlmostEqual(suma[1], 11.8)

if __name__ == '__main__':
    unittest.main()