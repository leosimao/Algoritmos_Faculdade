import random as rd
from time import sleep
#Parametros
#1. Faça uma procedimento que soma dois números. Deve ser utilizado um procedimento chamado somar(), que deve receber os números a serem somados, somar os números e apresentar o resultado na tela.

def PrcSomar(a, b):
    value = a + b
    print(f"O resultado da soma é {value}")

#2. Faça um procedimento que multiplica dois números. Deve ser utilizado um procedimento chamado multiplicar(), que deve receber os números e realizar a operação de multiplicação, apresentando o resultado na tela.
def PrcMult(a, b):
    value = a * b
    print(f"O resultado da multiplicação é {value}")

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

#6. Crie um procedimento que recebe um vetor de números inteiros por parâmetro. Esta função deve chamar imprimirVetor() e vai imprimir na tela todos os números do vetor informado. 
def PrcImpVetor(vtr):
    print("Imprimindo vetor")
    for i in range(0, len(vtr)):
        print(vtr[i], " ", end = "")
        sleep(0.2)

#7. Faça um procedimento chamado encontrarMaior() que recebe um vetor de números inteiros como parâmetro, procure e informe somente o maior valor do vetor.
def PrcEncMaiorVetor(vtr):
    maior = vtr[1]
    for i in range(0, len(vtr)):
        if(vtr[i] > maior):
            maior = vtr[i]
    print()
    print(f"O maior valor encontrado nesse vetor foi {maior}")

def PrcEncMenorVetor(vtr):
    menor = vtr[1]
    for i in range(0, len(vtr)):
        if(vtr[i] < menor):
            menor = vtr[i]
    print(f"O menor valor encontrado no vetor foi o {menor}")


vl1 = int(input("Digite o primeiro valor para somar: "))
vl2 = int(input("Digite o segundo valor para somar: "))

#def 1 até def 4

v = PrcSomar(vl1, vl2)
v = PrcMult(vl1, vl2)
print()
v = PrcRaiz(int(input("Digite o valor que queira saber a raiz quadrada: ")))
print()
v = PrcPotencia(vl1, vl2)
print()
#def 5
tab = int(input("Digite a tabuada que devemos retornar: "))
PrcTabuada(tab)

#def 6

v = [0] * rd.randint(10, 20)
for j in range(0, len(v)):
    v[j] = rd.randint(0, 200)

sleep(0.2)

PrcImpVetor(v)
print()
sleep(0.2)
#def 7 e exercicio 3
PrcEncMaiorVetor(v)
PrcEncMenorVetor(v)