#lista é com colchetes
estudants_list = ["Mateus", 24, "Fernanda", 22, "Tamires", 26, "Cristiano", 25]
print(estudants_list)

#dicionario é com chaves
estudantes_dict = {"Mateus":24, "Fernanda":22, "Tamires":26, "Cristiano":25}
print(estudantes_dict)
#consultando dicionario
print(estudantes_dict["Mateus"])
print(estudantes_dict["Fernanda"])

#deletar item do dicionario
del estudantes_dict["Tamires"]
print(estudantes_dict)

#contar numero de itens no dicionario
estudantes_dict = {"Mateus":24, "Fernanda":22, "Tamires":26, "Cristiano":25}
print(len(estudantes_dict))

#retornar apenas palavras-chave do dicionario
print(estudantes_dict.keys())

#retornar apenas valores do dicionario
print(estudantes_dict.values())

#retornar dicionario como itens
print(estudantes_dict.items())

#atualizando dicionario
estudants_2 = {'Maria': 27, 'Erika': 28, 'Milton': 26}
estudantes_dict.update(estudants_2)
print(estudantes_dict)

#acessando itens no dicionario
dict3 = {'key1':1230,'key2':[22,453,73.4],'key3':['leite','maça','batata']}
print(dict3['key3'])
print(dict3['key3'][0].upper())
