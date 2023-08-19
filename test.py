import math
import unittest
import cplx_lib

class Test_cplx_functions(unittest.TestCase):

    def test_suma(self):
        # 1. (3+2i) + (-5+5.2i) = (-2+7.2i)
        c1 = (3,2)
        c2 = (-5,5.2)
        self.assertAlmostEqual(cplx_lib.suma_cplx(c1,c2),(-2,7.2))
        # 2. (3+5i) + (-2.6+6.8i) = (0.4 + 11.8i)
        suma = cplx_lib.suma_cplx((3,5),(-2.6,6.8))
        self.assertAlmostEqual(suma[0], 0.4)
        self.assertAlmostEqual(suma[1], 11.8)
    def test_resta(self):
        # 1. (5.6+ 5i) - (-2+3.6i) = (7.6-8.6i)
        a = (5.6,-5)
        b = (-2,3.6)
        self.assertAlmostEqual(cplx_lib.resta_cplx(a, b), (7.6,-8.6))
        # 2. (1-2.5i) - (-8-6i) = (9+3.5i)
        a = (1, -2.5)
        b = (-8, -6)
        self.assertAlmostEqual(cplx_lib.resta_cplx(a, b), (9, 3.5))
    def test_multi(self):
        # 1. (1+2i) x (5+6i) = (17+4i)
        a = (1, 2)
        b = (5, -6)
        self.assertAlmostEqual(cplx_lib.multi_cplx(a, b), (17, 4))
        # 2. (1+2i) x (3+4i) = (-5+10i)
        a = (1, 2)
        b = (3, 4)
        self.assertAlmostEqual(cplx_lib.multi_cplx(a, b), (-5, 10))
    def test_divi(self):
        # 1. (6-2i) + (3+4i) = (2/5-6/5i)
        a = (6,-2)
        b = (3,4)
        self.assertAlmostEqual(cplx_lib.divi_cplx(a,b), (2/5, -6/5))
        # 2. (2-2i) + (7+10i) = (-6/149-34/149i)
        a = (2, -2)
        b = (7, 10)
        self.assertAlmostEqual(cplx_lib.divi_cplx(a, b), (-6/149, -34/149))
    def test_mod(self):
        # 1. (2+3i) = sqrt(13)
        a = (2,3)
        self.assertAlmostEqual(cplx_lib.mod_cplx(a), math.sqrt(13))
        # 2. (-3+4i) = sqrt(7)
        a = (1/math.sqrt(2),-7/math.sqrt(2))
        self.assertAlmostEqual(cplx_lib.mod_cplx(a), 5)
    def test_conj(self):
        # 1. (2.5-3i) = (2.5+3i)
        conj_1 = cplx_lib.conj_cplx((2.5,-3))
        self.assertAlmostEqual(conj_1[0], 2.5)
        self.assertAlmostEqual(conj_1[1], 3)
        # 2. (-5+7.2i) = (-5-7.2i)
        conj_2 = cplx_lib.conj_cplx((5, 7.2))
        self.assertAlmostEqual(conj_2[0], 5)
        self.assertAlmostEqual(conj_2[1], -7.2)
    def test_carte(self):
        # 1. (5, 30) = (4.3+2.5i)
        carte_1 = cplx_lib.repre_cartesiana((5, 30))
        self.assertAlmostEqual(carte_1[0], carte_1[0]*math.cos(carte_1[1]))
        self.assertAlmostEqual(carte_1[1], carte_1[0]*math.sin(carte_1[1]))

if __name__ == '__main__':
    unittest.main()