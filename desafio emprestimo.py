salario = float(input("insira seu salario para avaliarmos o emprestimo: "))
emprestimo = float(input("insira a quantidade que deseja pegar no emprestimo: "))

if (emprestimo <= salario*0.5):
    print("emprestimo aprovado")
    
elif (emprestimo <= salario*0.75):
    print("emprestimo em analise")
    
else:
    print("emprestimo não aprovado")