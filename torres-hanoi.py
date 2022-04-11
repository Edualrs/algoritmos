# cabeçalho
print('''
TORRES DE HANÓI

     |    |    |
    -|-   |    |
   --|--  |    |
  ---|--- |    |
 ===================

Regras: apenas um disco poderá ser movido por vez e nunca um disco maior deverá ficar por cima de um disco menor.

Objetivo: informando quantos discos existem no jogo, você deve obter a quantidade de movimentos necessários para movimentar todos os discos para uma outra haste.
--------------------
''')

# obtendo número de discos
discos = int(input('Quantidade de discos: '))
print('\n--------------------')

# verificando se o valor obtido é válido
if (discos >= 3):
    # caso sejá, realiza o cálculo de movimentos
    movimentos = (2 ** discos) - 1
    print('\nA quantidade de movimentos necessários para mover todos os discos para uma outra haste é {}\n'.format(movimentos))
else:
    # caso contrário, informa que o valor é inválido
    print('\nNúmero de discos inválido\n')
