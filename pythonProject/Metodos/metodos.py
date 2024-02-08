
list = [100, -2, 12, 65, 0]
print(list)

# Usando um método do objeto lista
list.append(10)
print(list)

# Usando um método do objeto lista
list.count(10)
print(list)

# A função help() explica como utilizar cada método de um objeto
list = [100, -2, 12, 65, 0]
print(help(list.count))

# A função dir() mostra todos os métodos e atributos de um objeto
list = [100, -2, 12, 65, 0]
print(dir(list))


# O método de um objeto pode ser chamado dentro de uma função, como print()
a = 'Isso é uma string'
print (a.split())