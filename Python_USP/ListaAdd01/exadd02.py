n = int(input('Por favor, entre com o número de segundos que deseja converter: '))
a = n // 86400 # Converte em dia
rsa = n % 86400 # Segundos restantes da conversão em dia
b = rsa // 3600 # Converte em horas
rsb = rsa % 3600 # Segundos restantes da conversão em horas
c = rsb // 60 # Converte em minutos
d = rsb % 60 # Segundos restantes da conversão em minutos
print('{} dias, {} horas, {} minutos e {} segundos.'.format(a, b, c, d))
