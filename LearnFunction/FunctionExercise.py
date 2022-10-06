#Parametros
#1. Faça uma procedimento que soma dois números. Deve ser utilizado um procedimento chamado somar(), que deve receber os números a serem somados, somar os números e apresentar o resultado na tela.

def PrcSomar(a, b):
    value = a + b
    print(f"O resultado da soma é {value}")

#2. Faça um procedimento que multiplica dois números. Deve ser utilizado um procedimento chamado multiplicar(), que deve receber os números e realizar a operação de multiplicação, apresentando o resultado na tela.
def PrcMult(a, b):
    value = a * b
    print(f"O resultado da multiplicação é {PrcMult}")

#3. Faça um procedimento que calcule a raiz quadrada de um número chamado calcularRaiz(). O procedimento deve receber o número por parâmetro, efetuar o cálculo e apresentar o resultado.
def PrcRaiz(a):
    value = a ** 0.5
    print(f"A raiz quadra de {a} é igual a {value}")

#4. Faça um procedimento que calcule a potência de um número (XY) chamado calcularPotencia(). O procedimento deve receber os números por parâmetro, efetuar o cálculo e apresentar o resultado.
def PrcPotencia (a, b):
    value = a ** b
    print(f"A potência de {a} elevado por {b} é igual a {value}")

#5. Faça um procedimento que calcule a tabuada de 1 a 10 para um número chamado calcularTabuada(). O procedimento deve receber o número por parâmetro, efetuar o cálculo e apresentar o resultado.
def PrcTabuada(a):
    for i in range (1, 11):
        v = a * i
        print(f"{a} x {i} = {v}")

vl1 = int(input("Digite o primeiro valor para somar: "))
vl2 = int(input("Digite o segundo valor para somar: "))
v = PrcSomar(vl1, vl2)
print(f"A soma de {vl1} + {vl2} = {v}")
print()
tab = int(input("Digite a tabuada que devemos retornar: "))
PrcTabuada(tab)
