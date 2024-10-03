#sintaxe Básica
def nome_da_funcao(parametros):
    #bloco de codigo
    return()
#<---------------------------------------------------------->
# def saudacao():
#     print("Olá, bem-vindo(a) à aula de funções em python!")

# saudacao()
#<---------------------------------------------------------->
# def saudacao(nome= "aluno"): #'nome' é um parametro
#     print(f"olá {nome}")
# saudacao() #'aluno' vira um valor padrão
# #se eu definir oque eu quero ele sobscreve o valor
# saudacao("Marcelo") #'Marcelo' é um argumento

#<---------------------------------------------------------->
# def somar(a,b): #recebendo mais de 1 parametro
#     return a + b
# resultado = somar(10, 20)
# print(resultado)
#<---------------------------------------------------------->
# def checar_numero(n):
#     if n > 0:
#         return "Positivo"
#     elif n < 0:
#         return "Negativo"
#     else:
#         return "Zero"
    
# num = int(input("insira um numero para verificar se ele epositivo ou negativo: "))
# print(checar_numero(num))
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
    print("Detalhes do pedido obtidos.")
    return pedido

def calcular_preço_total(pedido):
    #calcular o preço total do pedido
    preco_total = pedido['preco'] *pedido['quantidade']
    print(f"Preço total calculado: R${preco_total}")
    return preco_total

def enviar_confirmação(pedido, preco_total):
    #simula o envio de uma confirmação de pedido
    print(f"Confirmação enviada para {pedido['quantidade']} {pedido['item']}(s).")
    print(f"Valor total a ser pago: R$ ")