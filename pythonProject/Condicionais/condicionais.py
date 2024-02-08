# Condicional IF
if 5 > 2:
    print("Funciona!")

# Condicional IF...ELSE
if 5 < 2:
    print("Funciona!")
else:
    print("Algo está errado!")

# Condicionais aninhados

idade = 18
if idade > 17:
    print("Maior de idade!")

Nome = "Bob"
if idade > 15:
    if Nome == "Bob":
        print("Bob é maior de idade!")
    else:
        print("Bob é menor de idade!")

idade = 18
Nome = "Bob"
if idade >= 18 and Nome == "Bob":
    print("Ok Bob, você pode dirigir!")

idade = 12
Nome = "Bob"
if (idade <= 18) or (Nome == "Bob"):
    print("Desculpe Bob, mas você não pode dirigir!")

#Condicional ELIF

dia = "Terça"
if dia == "Domingo":
    print("Hoje tem aula!")
else:
    print("Hoje não tem aula!")

if dia == "Segunda":
    print("Hoje tem aula!")
elif dia == "Domingo":
    print("Hoje não tem aula")
else:
    print("Hoje é feriado!")

# Usando mais de uma condição na cláusula if

disciplina = input('Digite o nome da disciplina: ')
nota_final = input('Digite a nota final (entre 0 e 100): ')

if disciplina == 'Geografia' and nota_final >= '70':
    print('Você foi aprovado!')
else:
    print('Lamento, acho que você precisa estudar mais!')

# Usando mais de uma condição na cláusula if e introduzindo Placeholders

disciplina = input('Digite o nome da disciplina: ')
nota_final = input('Digite a nota final (entre 0 e 100): ')
semestre = input('Digite o semestre (1 a 4): ')

if disciplina == 'Geografia' and nota_final >= '50' and int(semestre) != 1:
    print('Você foi aprovado em %s com média final %r!' % (disciplina, nota_final))
else:
    print('Lamento, acho que você precisa estudar mais!')