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

def repre_cartesiana(c1):
    """representacion cartesiana de un numero complejo
    (real, angulo) -> (cplx)
    """
    a = c1[0]*math.cos(c1[1])
    b = c1[0]*math.sin(c1[1])
    return a, b

def repre_polar(c1):
    """representacion polar de un numero complejo
    (cplx) -> (real, angulo)
    """
    r = mod_cplx(c1)
    angle = math.atan2(c1[1],c1[0])
    return r, angle

def fase_cplx(c1):
    """fase o argumento de un numero complejo
    (cplx) -> real
    """
    fase = math.atan2(c1[1], c1[0])
    return fase