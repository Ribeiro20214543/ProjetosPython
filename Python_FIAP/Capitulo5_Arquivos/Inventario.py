from Funcoes.Funcoes_Arquivos import *
inventario = {}
opcao = chamarMenu()
while opcao > 0 and opcao < 4:
    if opcao == 1:
        registrar(inventario)
    elif opcao == 2:
        persistir(inventario)
    elif opcao == 3:
        resultado = exibir()
        for linha in resultado:
           # print(linha[2:-1]) # slice - recortar um string
           # ou podemos fazer assim:
            # print(linha[linha.find(";")+1:-1]) # find - encontra a posição do primeiro ; e acrescenta + 1
           # ou podemos fazer assim:
               separacao = linha[linha.find(";") + 1:-1]
               data = separacao[0:separacao.find(";")]
               separacao = separacao[separacao.find(";") + 1:-1]
               descricao = separacao[0:separacao.find(";")]
               departamento = linha[linha.rfind(";") + 1:-1]
               print("Data.........: ", data)
               print("Descrição....: ", descricao)
               print("Departamento.: ", departamento)
        # ou podemos fazer melhor assim:
              #  lista = linha.split(";")
              # print("Data.........: ", lista[1])
              #  print("Descrição....: ", lista[2])
              #  print("Departamento.: ", lista[3])
        opcao = chamarMenu()
