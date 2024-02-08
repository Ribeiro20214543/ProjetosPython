# Importando um módulo em Python
import math

# Verificando todos os métodos disponíveis no módulo
dir(math)
print(dir(math))

# Usando um dos métodos do módulo math
math.sqrt(25)
print(math.sqrt(25))

# Importando apenas um dos métodos do módulo math
from math import sqrt

# Usando o método
sqrt(9)
print(sqrt(9))

import random
random.choice(['Maça', 'Banana', 'Laranja'])
print(random.choice(['Maça', 'Banana', 'Laranja']))
random.sample(range(100), 10)
print(random.sample(range(100), 10))

import statistics
dados = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
print(statistics.mean(dados))
print(statistics.median(dados))

import os
print(os.getcwd())
print(dir(os))

import sys
print(sys.stdout.write('Teste'))
print(sys.version)
print(dir(sys))

# Importando o módulo request do pacote urllib, usado para trazer url's
# para dentro do nosso ambiente Python
import urllib.request

# Variável resposta armazena o objeto de conexão à url passada como
# parâmetro
resposta = urllib.request.urlopen('http://python.org')

# Objeto resposta
print(resposta)

# Chamando o método read() do objeto resposta e armazenando o código
# html na variável html
html = resposta.read()

# Imprimindo html
print(html)