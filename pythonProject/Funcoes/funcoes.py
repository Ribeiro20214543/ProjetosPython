# Definindo uma função
def primeiraFunc():
    print('Hello World')
primeiraFunc()

# Definindo uma função com parâmetro
def primeiraFunc(nome):
    print('Hello %s' %(nome))
primeiraFunc('Aluno')

def funcLeitura():
    for i in range(0, 5):
        print("Número " + str(i))
funcLeitura()

# Função para somar números
def addNum(firstnum, secondnum):
    print("Primeiro número: " + str(firstnum))
    print("Segundo número: " + str(secondnum))
    print("Soma: ", firstnum + secondnum)

# Chamando a função e passando parâmetros
addNum(45, 3)

# Variável Global
var_global = 10  # Esta é uma variável global

def multiply(num1, num2):
    var_global = num1 * num2  # Esta é uma variável local
    print(var_global)

multiply(5, 25)

print(var_global)

#Funções Built-in
print(abs(-56))
print(abs(23))
print(bool(0))
print(bool(3))

#Funções str, int, float
# Usando a função int para converter o valor digitado
idade = int(input("Digite sua idade: "))
if idade > 13:
    print("Você pode acessar o Facebook")


