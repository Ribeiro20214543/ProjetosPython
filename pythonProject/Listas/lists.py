#criando lista
list1 = ["sabonete, farinha, leite, azeite, suco"]
print(list1)

#lista com aspas
list2= ["sabonete", "farinha", "ovo", "suco"]
print(list2)

#lista com numeros
list3 = [24, 16, 19, "Rua"]
print(list3)

#atribuindo valor da lista a uma variavel
item1 = list3[0]
item2 = list1
item3 = list2[3]
print(item1, item2, item3)

#atualizando lista
print(list2[2])

#atualizando um item da lista
list2[2] = "chocolate"
print(list2)

#deletando um item da lista
del list2[3]
print(list2)

#lista alinhadas
list4 = [[1, 2, 3], [10, 15, 14], [10.1, 8.7, 2.3]]
print(list4)

#atribuindo um item da lista a uma variavel
a = list4[0]
print(a)

b = a[0]
print(b)

list1 = list4[1]
print(list1)

valor_1_0 = list1[0]
print(valor_1_0)

c = list4[2][2]
print(c)

d = c + 10
print(d)

e = d - 2
print(e)

f = e * 2
print(f)

#concatenando listas
list_total= list2 + list3
print(list_total)

#verificando se um valor pertence a lista
list_test = [25, 30, 5.4, 120, -3]
print(25 in list_test)
print(10 in list_test)

#retorna o total de itens na lista
print(len(list_test))

#retorna o maior numero da lista
print(max(list_test))

#retorna o menor numero da lista
print(min(list_test))

#add um item na lista
list2.append("carne")
print(list2)

#conta um item da lista
list2.append("carne")
print(list2.count("carne"))

#copiando itens de uma lista para a outra
list_a = ["sabonete", "farinha", "ovo", "suco"]
list_b = ["banana", "bebida", "amaciante"]
new_list = []
print(list_a)
print(list_b)
print(new_list)
for item in list_b + list_a:
    new_list.append(item)
print(new_list)

#extendendo itens de uma lista
cities = ['Curitiba', 'Santos', 'Manaus', 'Fortaleza']
cities.extend(['São Paulo', 'Guarulhos'])
print(cities)

#indexando itens de uma lista
print(cities.index('Santos'))

#insertando itens de uma lista
cities.insert(2, 120)
print(cities)

#removendo itens de uma lista
cities.remove(120)
print(cities)

#revertendo a ordem  itens de uma lista
cities.reverse()
print(cities)

#ordenando itens da lista
x = [3, 5, 4, 1, 2]
print(x)
x.sort()
print(x)

