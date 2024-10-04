#sintaxe Básica
def nome_da_funcao(parametros):
    #bloco de codigo
    return()
#<---------------------------------------------------------->
def saudacao():#criando um função
    print("Olá, bem-vindo(a) à aula de funções em python!")#inserindo o codigo que a função utilizara

saudacao()#chamando a função
# <---------------------------------------------------------->
def saudacao(nome= "aluno"): #'nome' é um parametro
    print(f"olá {nome}")
saudacao() #'aluno' vira um valor padrão
#se eu definir oque eu quero ele sobscreve o valor
saudacao("Marcelo") #'Marcelo' é um argumento

#<---------------------------------------------------------->
def somar(a,b): #recebendo mais de 1 parametro
    return a + b#retornando os parametros (a,b) para somar eles fora da função
resultado = somar(10, 20) #definindo os numeros que (a,b) representam
print(resultado)#output 30
#<---------------------------------------------------------->
def checar_numero(n):#criando um função que checa se um numero é positivo ou negativo
    if n > 0: #se o numero for maior que '0' ele é positivo
        return "Positivo"
    elif n < 0: # se o numero for menor que '0' ele é negativo
        return "Negativo"
    else:#se não for nenhuma da opções acima ele é zero
        return "Zero"
    
num = int(input("insira um numero para verificar se ele e positivo ou negativo: "))#pedindo para o usuario inserir o numero
print(checar_numero(num))
#<---------------------------------------------------------->
global_var = 100

def exemplo_escopo():
    local_var = "Estou dentro da função"
    print(local_var) #so existe dentro da função
    print(global_var) #existe fora da função e pode ser chamado em qualquer lugar do codigo
exemplo_escopo()
# print(local_var)
#<---------------------------------------------------------->
#argumentos posicionais:
#os argumentos são passados para a função na mesma ordem dos parametros.

def exibir_nome_idade(nome,idade):
    print(f"Nome: {nome}, Idade: {idade}")
    
exibir_nome_idade("Marcelo",17)
exibir_nome_idade(nome="Ruan",idade=17)
#<------------------------------------------------------------------------------------>
#Argumentos Arbritarios (*args e **kwargs):

#*args: Recebe múltiplos argumentos como uma tupla

def somar_todos(*args):
    return sum(args)

print(somar_todos(1,2,3,4,5,6,7,8,9,10,15)) #output 70

#**kwargs: Recebe múltiplos argumentos nomeados como um dicionário.
def exibir_detalhes(**kwargs):
    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")

exibir_detalhes(nome="Marcelo", idade= 17, cidade="Pernanbuco",telefone = 819839805062)
#<------------------------------------------------------------------------------------>
#função para Encontrar a soma dos números Pares usando o while:

def soma_pares(numeros):
    soma = 0 
    i = 0
    while i < len(numeros):
        if numeros[i] % 2 == 0:
            soma += numeros[i]
        i += 1
    return soma
print(soma_pares([1,2,3,4,5,6]))
#<----------------------------------------------------------------------------------------------------------->

def obter_detalhes_pedido():
    #simula a obtenção de detalhes do pedido
    pedido = {
        "item": "notebook",
        "preco": 1200.00,
        "quantidade": 2
    }
    pedido2 = {
        "item": "celular",
        "preco2": 2.3000,
        "quantidade": 3
    }
    print("Detalhes do pedido obtidos.")
    return pedido, pedido2

def calcular_preço_total(pedido,pedido2):
    #calcular o preço total do pedido
    preco_total = pedido['preco'] *pedido['quantidade']
    preco_total2 = pedido2['preco'] *pedido2['quantidade']
    
    print(f"Preço total do primeiro pedido calculado é calculado: R${preco_total}")
    print(f"Preço total do segundo pedido calculado é : R${preco_total2}")
    return preco_total, preco_total2

def enviar_confirmação(pedido, preco_total, pedido2, preco_total2):
    #simula o envio de uma confirmação de pedido
    print(f"Confirmação do primeiro pedido enviada para {pedido['quantidade']} {pedido['item']}(s).")
    print(f"Valor total a ser pago do primeiro pedido é: R$ {preco_total}")
    print(f"confirmção enviada do segundo pedido enviada para {pedido2['quantidade']} {pedido2['item']}(s) ")
    print(f"Valor total a ser pago do segundo pedido é: R$ {preco_total2}")
    
def processar_pedido():
    pedido = obter_detalhes_pedido()
    preco_total = calcular_preço_total(pedido)
    enviar_confirmação(pedido,preco_total)
    
    pedido2 = obter_detalhes_pedido()
    preco_total2 = calcular_preço_total(pedido2)
    enviar_confirmação(pedido2,preco_total2)
    
processar_pedido()