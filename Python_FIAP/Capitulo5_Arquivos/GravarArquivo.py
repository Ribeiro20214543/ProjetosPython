#Escreve Arquivo
with open("teste.txt", "w") as arquivo:
  arquivo.write("Nunca foi tão fácil criar um arquivo.")

with open("teste.txt", "w") as arquivo:
  arquivo.write("Continuação do texto.")

# Ler Arquivo
with open("teste.txt", "r") as arquivo:
  conteudo = arquivo.read()

print(conteudo)