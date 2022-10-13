import random as rd
from time import sleep as sp
#Functions
#1. Crie uma função para pedir um número inteiro ao usuário e retornar ele. Toda vez que você precisar de um número informado pelo usuário, utilize ela. Ela não tem parâmetro e o retorno é o valor digitado pelo usuário já com o tipo inteiro.

def NumInt ():
    v = int(input("Digite o número desejado: "))
    return v

def aleatorio(value):
    a = rd.randint(1, value)
    return a

def mes(month):
    mt = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
    if(month >= 1 and month <= 12):
        val = True
        for i in range(0, len(mt) + 1):
            if(month - 1 == i):
                m = print(f"O mês escolhido foi {mt[i]}")
                return m
def calculos():   
    opt = 0
    while(opt != 5):
        menu = print(
        """==== MENU ====
        1. Função quadrado
        2. Função do Retangulo
        3. Função do Triangulo
        4. Função do Trapézio  
        5. Sair
        """)
        opt = int(input("Digite a opção desejada: "))
        if(opt == 1):
            qd = int(input("Escolha um número para ser elevado ao quadrado: "))
            result = qd ** 2
            result = print(f"O resultado de {qd} ^ 2 é {result}")
        elif(opt == 2):
            print("Para realizar esse calculo precisaremos da Base b e altura h")
            b = float(input("Base: "))
            h = float(input("Altura: "))
            result = b * h
            result = print(f"A área do retangulo é igual a {result}")
        elif(opt == 3):
            print("Para calcular a área do triangulo deve-se digita qual é a base do triangulo e sua altura")
            b = float(input("Base: "))
            h = float(input("Altura: "))
            result = (b * h) / 2
            result = print(f"A área do triangulo é igual a {result}")
        elif(opt == 4):
            t = False
            print("Para ser calculado a área do trapézio deve-se dar a base maior, base menor e e altura")
            b1 = float(input("Base Maior: "))
            while(t != True):
                b2 = int(input("Base menor: "))
                if(b2 > b1):
                    print(f"A base menor é maior que a Base maior, digite um valor válido para base menor!")
                else:
                    t = True
            h = float(input("Altura: "))
            result = ((b1 + b2) * h) / 2
            result = print(f"A área do trapézio é igual a {result}")
        elif(opt == 5):
            result = print("Obrigado por participar!")
    return result       

def fatorial(value):
    while(value <= 0):
        print("Número menor ou igual a 0 não é permitido, tente novamente")
        value = int(input("Digite o valor para que seja calculado o fatorial:"))
        print()
    if(value == 1):
        result = value * 1
        return result
    else:
        for i in range(value - 1, 0, -1):
            value *= i
    return value



valor = NumInt()
aleat = aleatorio(valor)
print(f"O valor escolhido foi {valor}")
print(f"O número aleatório entre 1 e {valor} foi , {aleat}")
print()
sp(2)
#3. Faça uma função que receba um número inteiro por parâmetro e retorne o mês correspondente ao número. Por exemplo, 2 corresponde a "Fevereiro". Se o número informado não corresponder a um mês (1 a 12), retorne a mensagem “Mês inválido”.
print("==== RETORNA MES ====")
val = False
while(val != True):
    user = int(input("Digite o número do mês desejado: "))
    if(user >= 1 and user <= 12):
        val = True
        month = mes(user)
    else:
        print("Mês invalido tente novamente!")
print("=====================")
print()
sp(2)
#4. Faça funções para resolver as equações de área:
valor = calculos()
print()
sp(2)
fat = int(input("Digite o valor para que seja calculado o fatorial: "))
rFat = fatorial(fat)
print(f"O resultado do fatorial de {fat} é igual a {rFat}")