#criando uma tupla - é com parenteses
tupla1 = ("Biologia", 23, "Urso")
print(tupla1)

#consultando tupla
print(tupla1[0])
print(tupla1[2])

#retornar o tamanho da tupla
print(len(tupla1))

#retornar slicing da tupla
print(tupla1[:1])
print(tupla1[1:])

#indexar uma tupla
print(tupla1.index('Urso'))

#deletando tupla
del tupla1
#OBS: print(tupla1) retorna erro

#convertendo tupla em lista
tupla2 = ("Biologia", 23, "Urso")
lista1 = list(tupla2)
print(lista1)

#convertendo lista em tupla
tupla3 = tuple(lista1)
print(tupla3)
