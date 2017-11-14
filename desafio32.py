#32º Desafio: Programa que leia um ano e mostre se ele é bissexto
print('========DESAFIO32========')
from datetime import date

ano = int(input('Digite um ano, coloque 0 para o ano atual: '))

if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('{} é um ano bissexto'.format(ano))
else:
    print('{} não é um ano bissexto!'.format(ano))