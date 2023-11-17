import math
def calc_quadratic_formula(a, b, c):
    discriminant = pow(b, 2) - 4 * a * c

    if discriminant > 0: #Cuando el determinante es mayor que 0, raices reales
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return root1, root2
    elif discriminant == 0: #Cuando el determinante es igual a 0, indica soluciones iguales, por lo tanto: x= (-b) / (2 * a)
        root = -b / (2 * a)
        return root
    else: # Si el determinante es negativo, indica raices imaginarias, por lo tanto: (-b) +/- (i) {sqrt(abs[ pow(b, 2) - (4*a*c) ])}
        real_part = -b / (2 * a)
        imaginary_part = math.sqrt(abs(discriminant)) / (2 * a) # Abs() retorna valor absoluto de un numero complejo
        root1 = complex(real_part, imaginary_part) # Compex() sirve para representar raices imaginarias, donde la parte real: (-b) / (2 * a)
        root2 = complex(real_part, -imaginary_part) # y la parte imaginaria: sqrt(abs[ pow(b, 2) - (4*a*c) ]) / (2 * a)
        return root1, root2