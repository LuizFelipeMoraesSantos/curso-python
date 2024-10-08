#sintaxe básica:
class NomeDaClasse:
    #Definição da classe
    pass

#exemplo 

class Pessoa:
    pass
Pessoa1 = Pessoa()
Pessoa2 = Pessoa()

#Exemplo
class Pessoa: #criaçõ de classes
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
Pessoa1 = Pessoa("Maria", 30)
print(Pessoa1.nome) #Saída: Maria
print(Pessoa1.idade) #Saída: 30

pessoa2 = Pessoa("Chico", 23)
print(pessoa2.nome)#Saída: Chico
print(pessoa2.idade)#Saida: 23

#exemplo

class Pessoas:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
        
    def apresentar(self):
        print(f"ola, meu nome é {self.nome} e tenho {self.idade} anos")
        
pessoa1 = Pessoas("Marcelo", 17)
print(pessoa1.nome)
print(pessoa1.idade)
pessoa1.apresentar()    

class Data_Nascimento:
    def __init__(self,data):
        self.data = data
        
    def nascimento(self):
        print(f"Eu nasci no ano de {self.data}")

pessoa =  Data_Nascimento(2024- int(input("insira sua idade")))

pessoa.nascimento()
        
class Cachorro_Quente():
    def __init__(self,ingrediente1,ingrediente2,ingrediente3):
        self.ingrediente1 = ingrediente1
        self.ingrediente2 = ingrediente2
        self.ingrediente3 = ingrediente3
        
    def apresentar(self):
            print(f"os ingredientes do cachorro quente são: {self.ingrediente1}, {self.ingrediente2} é {self.ingrediente3}")

ingrediente = Cachorro_Quente("pão","salsicha","batata palha")
print(ingrediente.ingrediente1)
print(ingrediente.ingrediente2)
print(ingrediente.ingrediente3)

ingrediente.apresentar()

        