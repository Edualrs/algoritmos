# Cabeçalho
print('''
ÁREA DO TRIÂNGULO

Fórmula:

A = (b * h) / 2 

A - Área    b - base    h - altura
--------------------
''')

# Obtendo valores da base e altura
b = float(input('Qual o valor da base do triângulo: '))
h = float(input('Qual o valor da altura do triângulo: '))

print('\n--------------------')

# Realizando cálculo para obtenção da área do triângulo
A = (b * h) / 2

# Apresentando valor em formato float com duas casas decimais
print('O valor da área do triângulo é de %.2f \n' % (A))
