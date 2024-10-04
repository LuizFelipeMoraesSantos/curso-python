#1. Crie uma função chamada saudacao() que recebe um nome como parâmetro e retorna uma saudação personalizada.
def saudacao(nome):#criando a função com o parametro nome
    print(f"ola {nome}, seja bem vindo!!")#imprimindo uma mensagem de bem vindo chamando o parametro em uma f-string

n = input("insira seu nome: ")#pedindo para o usuario inserir o nome
saudacao(n)#chamando a função e utilizando a varialvel (n) como argumento da função

#2.Escreva uma função soma() que recebe dois números como parâmetros e retorna a soma deles.
def soma(a,b):#criando uma função que receb 2 parametros
    return a + b#retornando os parametros para uslos fora da função

a = float(input("insira o numero que deseja somar: "))#pedindo para o usuario inserir oo numeros que deseja somar
b = float(input("insira o numero que deseja somar: "))
print(f"o resultado é: {soma(a,b)}")#imprimindo o resultado com base no que o usuario inseriu

#3.Escreva uma função fatorial() que recebe um número inteiro positivo como parâmetro e retorna o fatorial desse número.
def fatorial(numero):
    resultado = 1
    for i in range(1, numero + 1):
        resultado *= i
    return resultado
n = int(input("insira o numero que deseja saber o fatorial: "))
resultado = fatorial(n)
print(f"A fatorial de {n} é {resultado}") 