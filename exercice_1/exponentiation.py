def exponentiation(x, n):
    if n == 0:
        return 1
    elif n == 1:
        return x
    else:
        tmp = exponentiation(x, n/2)
        if n %2 == 0:
            return tmp * tmp
        else:
            return x * tmp * tmp

x = float(input('Nombre entier ou réel : '))
n = int(input('Nombre entier positif : '))

print(exponentiation(x, n))


