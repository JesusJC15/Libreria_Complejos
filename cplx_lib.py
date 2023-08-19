import math

def suma_cplx(c1, c2):
    """suma de complejos
    (cplx, cplx -> cplx)
    """
    parte_r = c1[0] + c2[0]
    parte_i = c1[1] + c2[1]
    return parte_r, parte_i


def resta_cplx(c1, c2):
    """resta de complejos
    (cplx, cplx -> cplx)
    """
    parte_r = c1[0] - c2[0]
    parte_i = c1[1] - c2[1]
    return parte_r, parte_i


def multi_cplx(c1, c2):
    """multiplicacion de complejos
    (cplx, cplx -> cplx)
    """
    parte_r = (c1[0] * c2[0]) - (c1[1] * c2[1])
    parte_i = (c1[0] * c2[1]) + (c2[0] * c1[1])
    return parte_r, parte_i


def divi_cplx(c1, c2):
    """division de complejos
    (cplx, cplx -> cplx)
    """
    parte_r = ((c1[0] * c2[0]) + (c1[1] * c2[1])) / (c2[0] * (c2[0]) + (c2[1] * c2[1]))
    parte_i = ((c2[0] * c1[1]) - (c1[0] * c2[1])) / (c2[0] * (c2[0]) + (c2[1] * c2[1]))
    return parte_r, parte_i


def mod_cplx(c1):
    """modulo de un numero complejo
    (cplx -> real)
    """
    modulo = math.sqrt((c1[0] * c1[0]) + (c1[1] * c1[1]))
    return modulo


def conj_cplx(c1):
    """conjugado de un numero complejo
    (cplx -> cplx)
    """
    parte_r = c1[0]
    parte_i = -(c1[1])
    return parte_r, parte_i