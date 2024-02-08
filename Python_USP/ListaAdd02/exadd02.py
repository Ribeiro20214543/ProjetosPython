import math
a = float(input('Digite o valor de a: '))
b = float(input('Digite o valor de b: '))
c = float(input('Digite o valor de c: '))
#calculando delta
delta = b ** 2 - 4 * a * c
#analisando delta
if delta == 0:
    #encontrar x
    x = (-b + math.sqrt(delta)) / (2 * a)
    print("a raiz desta equação é {}".format(x))
else:
    if delta < 0:
        print("esta equação não possui raízes reais")
    else:
        # encontrar x e y
        x = (-b + math.sqrt(delta)) / (2 * a)
        y = (-b - math.sqrt(delta)) / (2 * a)
        if x < y:
            print('as raízes da equação são {:.2f} e {:.2f}'.format(x, y))
        else:
            print('as raízes da equação são {:.2f} e {:.2f}'.format(y, x))
