#Functions
#1. Crie uma função para pedir um número inteiro ao usuário e retornar ele. Toda vez que você precisar de um número informado pelo usuário, utilize ela. Ela não tem parâmetro e o retorno é o valor digitado pelo usuário já com o tipo inteiro.

def inteiro(value):
    v = int(value)
    return v

vlr = float(input("Digite o valor desejado: "))

fun = inteiro(vlr)

print(f"A parte inteira de {vlr} é igual a: {fun}")
