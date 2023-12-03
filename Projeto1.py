from datetime import datetime
import random


print('------ Bem Vindo a nossa empresa! ------')

nome = input('Digite seu nome:')
idade = input('Digite sua idade:')

data_do_registro = datetime.now()

cartoes = ['R$50,00','R$250,00','R$120,00']
cartao = random.choices(cartoes)

aniversario = datetime.strptime(input('Digite a data de seu aniversário: '), '%d/%m/%Y')

data_aniversario = datetime(2024, 12, 3)
dias_aniversario = datetime.now()


# MODULO 2 

print(f'Olá {nome}, seu registro foi concluído com sucesso no dia {data_do_registro.day}/{data_do_registro.month}/{data_do_registro.year}.\nParabéns, houve um sorteio e você ganhou um cartão de compras no valor de {cartao}')