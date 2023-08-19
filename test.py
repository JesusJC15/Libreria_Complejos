import unittest
import cplx_lib

class Test_cplx_functions(unittest.TestCase):

    def test_suma(self):
        # 1. (3 + 2i) + (-5 + 5.2i) = (-2 , 7.2i)
        c1 = (3,2)
        c2 = (-5,5.2)
        self.assertAlmostEqual(cplx_lib.suma_cplx(c1,c2),(-2,7.2))
        # 2. (3 + 5i) + (-2.6 + 6.8i) = (0.4, 11.8i)
        suma = cplx_lib.suma_cplx((3,5),(-2.6,6.8))
        self.assertAlmostEqual(suma[0], 0.4)
        self.assertAlmostEqual(suma[1], 11.8)
    def test_resta(self):
        # 1. (5.6 + -5i) - (-2 + 3.6i) = (7.6 , -8.6i)
        a = (5.6,-5)
        b = (-2,3.6)
        self.assertAlmostEqual(cplx_lib.resta_cplx(a,b), (7.6,-8.6))

if __name__ == '__main__':
    unittest.main()