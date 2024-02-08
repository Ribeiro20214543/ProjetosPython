#uso de aspas
string = "Frase em Python"
print(string)

string = 'Python'
print(string)

string = "Frase em 'Python'"
print(string)

#pulando linhas
print('Frase \nem \nPython')

#Imprimindo Elementos
string = 'Python'
print(string[0])
print(string[1])
print(string[2])
print(string[3])
print(string[4])
print(string[5])

# Retorna todos os elementos da string, começando pela posição
print(string[0:])
print(string[1:])
print(string[2:])
print(string[3:])
print(string[4:])
print(string[5:])

# Retorna tudo até a posição
print(string[:0])
print(string[:1])
print(string[:2])
print(string[:3])
print(string[:4])
print(string[:5])
print(string[:6])

#ler de trás para frente
print(string[-1])
print(string[-2])
print(string[-3])
print(string[-4])
print(string[-5])
print(string[-6])

# Retornar tudo, exceto
print(string[:-1])
print(string[:-2])
print(string[:-3])
print(string[:-4])
print(string[:-5])
print(string[:-6])

#mudar a sequencia das letras
print(string[::2])
print(string[::-2])

#concatenando
print(string + ' é usado em Ciência de Dados')
#ou
s = string + ' é usado em Ciência de Dados'
print(s)
#repetição
print(s * 3)

