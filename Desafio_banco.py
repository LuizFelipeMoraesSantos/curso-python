informações_cliente = {}

while True:
    print("1.Criar conta\n2.Verificar Saldo\n3.Depositar Dinheiro\n4.Sacar Dinheiro\n5.Encerrar Atendimento")
    opcao = input("Bem Vindo ao Banco!!\nInsira qual serviço deseja utiliza: ")
    
    if opcao == "1":
        def criar_conta():
            nome_user = (input("insira seu nome: "))
            senha_user = (input("Insira sua senha: "))
            informações_cliente[nome_user] = {"Senha": senha_user, "Saldo": 0}
            print(f"Conta criada com sucesso: {informações_cliente}")
            
        criar_conta()
        
    elif opcao == "2":
        def Verificar_saldo():
           nome_user = input("insira seu nome para verificar seu saldo: ")
           if nome_user in informações_cliente:
                saldo = informações_cliente[nome_user]["Saldo"]
                print(f"O saldo do cliente é: R${saldo:.3f}")
           else:
                print("Conta de usuario não existe")
                
        Verificar_saldo()
    
    elif opcao == "3":
        def Depositar_dinheiro():
            nome_user = input("insira seu nome para depositar o saldo: ")
            
            if nome_user in informações_cliente:
                depositar = float(input("Insira o valor que deseja depositar: "))
                informações_cliente[nome_user]["Saldo"] += depositar
                print(f"O deposito de {depositar:.3f} foi feito com sucesso")
            else:
                print("Conta de usuario não existe")
        Depositar_dinheiro()
    
    elif opcao == "4":
        def sacar_dinheiro():
            