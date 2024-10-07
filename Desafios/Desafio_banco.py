
informações_cliente = {}

while True:
    print("1.Criar conta\n2.Verificar Saldo\n3.Depositar Dinheiro\n4.Sacar Dinheiro\n5.Encerrar Atendimento") #criando um menu para instruir o usuario
    opcao = input("Bem Vindo ao Banco!!\nInsira qual serviço deseja utiliza: ") #input para o usuario escolher uma das opçoes do banco
    
    if opcao == "1": #se a opção for '1', o usuario cria uma conta nova no banco
        def criar_conta():
            nome_user = (input("insira seu nome: ")) #inserir o nome para cadastro
            senha_user = (input("Insira sua senha: ")) # inserir a senha para cadastro

            #criando um dicionario com a chave principal dele sendo o nome do usuario.
            #dentro do dicionario criado tem a chave(senha) que armazena a senha do usuario.
            #dentro tambem tem outra chave(saldo) que tem 0 por valor padrão.
            informações_cliente[nome_user] = {"Senha": senha_user, "Saldo": 0} 
            print(f"Conta criada com sucesso: {informações_cliente}")#impriminto o dicionario com a conta criada
            
        criar_conta() #chamando a função
        
    elif opcao == "2": #se a opção for '2', verificar o saldo da conta
        def Verificar_saldo():
            nome_user = input("insira seu nome para verificar seu saldo: ")# solicitando o nome de usuário para acessar o dicionario que guarda as informções do usuario.
            senha_user = input("insira sua senha: ")
            if nome_user in informações_cliente: #se o nome de usuario existir em 'informações_cliente'. seguir para o codigo abaixo
                if informações_cliente[nome_user]["Senha"] == senha_user: #verificando se senha do usuario esta correta
                    saldo = informações_cliente[nome_user]["Saldo"] #acessando o dicionario pela chave principal que é (nome_user) é chamando a chave que guarda o valor de saldo
                    print(f"O saldo do cliente é: R${saldo:.2f}") #imprimindo o valor atual de saldo
                else:
                    print("senha incorreta!! tente novamente")
            else:# caso o nome de usuario não existir em 'informações_cliente'. vai imprimir a mensagem abaixo.
                print("Conta de usuario não existe.")
                
        Verificar_saldo() #chamando a função
    
    elif opcao == "3":#se a opção for '3', Depositar dinheiro
        def Depositar_dinheiro():
            nome_user = input("insira seu nome para depositar o saldo: ")# solicitando o nome de usuário para acessar o dicionario que guarda as informções do usuario.
            senha_user = input("insira sua senha: ")
            if nome_user in informações_cliente:#se o nome de usuario existir em 'informações_cliente'. seguir para o codigo abaixo
                if informações_cliente[nome_user]["Senha"] == senha_user:
                    depositar = float(input("Insira o valor que deseja depositar: "))#pedindo para o usuario inserir o valor para executar o deposito
                    informações_cliente[nome_user]["Saldo"] += depositar #acessando a chave 'saldo' do dicionario é somando ela com o valor que o cliente inseriu em deposito
                    print(f"O deposito de {depositar:.2f} foi feito com sucesso.")#mensagem mostrando que o deposito foi bem sucedido
                
                else:
                    print("senha incorreta!! tente novamente")
            else:# caso o nome de usuario não existir em 'informações_cliente'. vai imprimir a mensagem abaixo.
                print("Conta de usuario não existe.")

        Depositar_dinheiro()#chamando a função
    
    elif opcao == "4":#se a opção for '4', sacar o dinheiro
        def sacar_dinheiro():
            nome_user = input("insira seu nome para Sacar o seu saldo: ")# solicitando o nome de usuário para acessar o dicionario que guarda as informções do usuario.
            senha_user = input("insira sua senha: ")
            if nome_user in informações_cliente:#se o nome de usuario existir em 'informações_cliente'. seguir para o codigo abaixo
                if informações_cliente[nome_user]["Senha"] == senha_user:
                    saldo = informações_cliente[nome_user]["Saldo"] #acessando a chave 'Saldo' para mostrar ao usuario o saldo disponivel
                    print(f"Saldo atual: {saldo:.2f}")#imprimindo o saldo atual
                    sacar = float(input("insira o valo que deseja Sacar: "))#pedindo para o usuario inserir qual o valor que deseja sacar
                
                    
                    if sacar > saldo: #se o valor do saque seja maior que o saldo da conta.imprime a mensagem abaixo
                        print("Impossível fazer o saque. Saldo insuficiente.")

                    else:#caso o valor do saque seja menor ou igual ao do saldo ele segue o codigo.
                        informações_cliente[nome_user]["Saldo"] -= sacar#acessando a chave 'Saldo' do dicionario é subtraindo com o valor inserindo no saque
                        print(f"O saque de: {sacar:.2f} da conta de {nome_user} foi feito com sucesso.") # mensagem mostrando que o saque foi um sucesso
                        print(f"Saldo Atual: R${informações_cliente[nome_user]["Saldo"]:.2f}")#imprimindo o saldo atual da conta

                else:
                    print("senha incorreta!! tente novamente")
            else:# caso o nome de usuario não existir em 'informações_cliente'. vai imprimir a mensagem abaixo.
                print("conta de usuario não existe.")
        sacar_dinheiro()#chamando a função

    elif opcao == "5":#se a opção for '5', ele sair do programa
        print("Saindo....")#imprimindo uma mensagem de saida
        break# parando o loop

    else:#caso não seja nenhuma das opções. imprime a mensagem abaixo
        print("Opçaõ invalida. tente novamente.")