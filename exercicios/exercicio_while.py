#crie um programa que imprima um numero de 1 a 10
contador = 1 #numero inicial
while contador <=10: #enquanto contador <= 10 ele vai imprimir os numeros ate cehgar 10
    print(contador)
    contador +=1    #a cada interação ele adiciona mais 1 no contador
    
# um programa que peça ao usuario para digitar uma senha e continue pedindo ate ele acertara senha correta
senha = 1234
tentativa = None
while tentativa != senha:
    tentativa = int(input("insira a senha de usuario: "))
    if tentativa != senha:
        print("senha incorreta, Tente novamente(dica: ela tem 4 digitos): ")
   
print("senha correta! seja bem vindo")

#solicitar ao usuario para inserir números inteiros ate que ele insira zero. e somar todos os numeros que ele inseriu
l = []
while True:
    soma = float(input("insira varios numeros para somar entre eles (insira '0' para somar todos eles): "))
    l.append(soma)
    if soma == 0:
        print(f"a soma dos numeros é {sum(l)}")
        break

#imprimir os 20 primeiros numeros pares usando while
pares = 1

while pares <= 20:
    pares +=1
    if pares %2 ==0:
        print(f"os numeros pares são {pares}")
    
#crie uma lista vazia e use o laço while para pedir ao usuario que adicione o nome na lista.O programa deve parar de adicionar nomes quando o usuairo escrever 'sair'
nomes = []
while True:
    nome = input("insira o nome que deseja adicionar na lista(insira sair para parar): ")
    if nome == "sair" or nome == "Sair":
        break
    nomes.append(nome)
print(nomes)
    
     
    
       
    
        
    
        