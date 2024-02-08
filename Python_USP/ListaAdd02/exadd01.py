import math
#Solicitando coordenadas dos pontos 1 e 2
x1 = float(input('Primeiro número: '))
y1 = float(input('Segundo número: '))
x2 = float(input('Terceiro número: '))
y2 = float(input('Quarto número: '))

#calculando a distância entre os dois pontos
x = (x1 - x2) ** 2
y = (y1 - y2) ** 2
distancia = math.sqrt(x + y)
print("A distância ente os dois pontos é de {:.2f} ".format(distancia))
#Analisando a distância
if distancia >= 10:
    print("longe")
else:
    print("perto")
