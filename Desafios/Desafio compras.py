#crie um programa que exiba um menu interativo com as seguintes opções:

# 1 - adicionar item
# 2 - Remover item
# 3 - Exibir lista
# 4 - Sair

#o programa deve permitir que o usuário gerencie uma lista de compras (compras = {}])
# cada opção deve realizar a ação correspondente até que o usuário escolha '4' para sair


carrinho = {"produtos": {} } #criando um dicionario vazio dentro de um dicionario para guarda os produtos é o preço

while True:
    escolha = (input("1 - adicionar item \n2 - Remover item \n3 - Exibir carrinho \n4 - Sair \nescolha a opção que deseja: "))
   
    if escolha == "1":
        produto = input("insira o produto que deseja adicionar ao carrinho: ")
        preços = float(input("insira o preço do produto escolhido: "))
        carrinho["produtos"][produto] = preços #acessando o dicionario para adiconar os produtos é os preços
        print(carrinho)
        
    elif escolha == "2":
        print(carrinho)
        
        deletar = input("digite o produto que deseja remover: ")
        if deletar in carrinho["produtos"]:
            del carrinho["produtos"][deletar]
            print(f"o produto ({deletar}) foi removido do carrinho")
            print(carrinho)
            
        else:
            print(f"O produto {deletar} não se encontra no carrinho")
        
    elif escolha == "3":
        print("os produtos no carrinho são: ",carrinho["produtos"])
        
    elif escolha == "4":
        print("saindo....")
        break

    else:
        print("opção, invalida")
    
    
    
    
