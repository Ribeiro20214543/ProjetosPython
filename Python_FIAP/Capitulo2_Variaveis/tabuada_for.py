tabuada = int(input("Digite um número para exibir a tabuada: "))
print("Tabuada do número ", tabuada)
for valor in range(1, 11, 1): #definido que os valores gerados estejam entre 1 e 11, com incremento de 1 em 1.
    print(str(tabuada) + " x " + str(valor) + " = " + str((tabuada*valor)))