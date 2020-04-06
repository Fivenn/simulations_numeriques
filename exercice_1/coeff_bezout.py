def coeff_bezout(a, b):
    if b == 0:
        return (1, 0)
    else:
        (u, v) = coeff_bezout(b, a % b)
        return (v, u-(a//b)*v)


a = int(input('a, un entier naturel :'))
b = int(input('b, un entier naturel :'))

res = coeff_bezout(a, b)

print('Coefficients de Bezout : {} et {}'.format(res[0], res[1]))
