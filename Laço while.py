import random
# exemplo:
while True:
    nome = input("Digite seu nome(ou 'sair' para parar): ")
    
    if nome == "sair" or nome == "Sair": #utilizando o 'or' para caso o usuario escreva "Sair" com letra maiuscula
        break #o break é utilizado para sair do laço quando a condição desejada for atiginda
    print(f"ola, {nome}") #o programa continuará pedindo ao usuario para digitar seu nome até que ele digite "sair"

# exemplo2:
numero_sercreto = random.randint(1, 21) #utilizando o modulo 'random.randint' para gerar um numero aleatorio de 1 á 100
tentativa = None

while tentativa != numero_sercreto:
    tentativa = int(input("Adivinhe o número (entre 1 e 20): "))
    if tentativa <= numero_sercreto:
        print(F"insira um numero maior que {tentativa}")
    elif tentativa >= numero_sercreto:
        print(f"insira um numero menor que {tentativa} ")
        
    elif tentativa == numero_sercreto:
        break
print("Parabens! Você adivinhou o número")

#crie um programa que continue pedindo para o usuario digitar
#dois numeros é a operação desejada(+,-,*,/).
#o laço deve parar quando o usuário digitar "sair"

while True:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o  segundo número: "))
    operacao = input("Digite a operação (+, -, *, /) ou sair para parar: ")
    
    if operacao == "sair":
        break
    
    if operacao == "+":
        print(f"resultado: {num1 + num2}")
    elif operacao == "-":
        print(f"Resultado: {num1 - num2}")
    elif operacao == "*":
        print(f"Resultado: {num1 * num2}")
    elif operacao == "/":
        if num2 == 0:
            print("erro: Divisão por zero")
        elif num1 == 0:
            print("erro: Divisão por zero")
        else:
            print(f"resultado: {num1 / num2}")
    else:
        print("operação invalida")
        

    


