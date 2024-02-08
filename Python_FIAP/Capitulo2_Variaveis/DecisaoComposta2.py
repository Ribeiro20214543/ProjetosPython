nome = input("Digite o nome: ")
idade = int(input("Digite a idade: "))
doenca_infectocontagiosa = input("Suspeita de doença infecto-contagiosa?").upper() #Converter o conteudo da string em letras maiusculas
if idade >= 65:
    print("O paciente " + nome + " POSSUI atendimento prioritário!")
elif doenca_infectocontagiosa == "SIM": #operação de comparacao
    print("O paciente " + nome + " deve ser direcionado para sala de espera reservada.")
else:
    print("O paciente " + nome + " NÃO possui atendimento prioritário e pode aguardar na sala comum!")