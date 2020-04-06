def exponentiation(x, n):
    if n == 1:
        return x
    elif n % 2 == 0:
        return exponentiation(x**2, n/2)
    else:
        return x * exponentiation(x**2, (n-1)/2)


x = float(input('Nombre entier ou réel : '))
n = int(input('Puissance : '))

print(exponentiation(x, n))
