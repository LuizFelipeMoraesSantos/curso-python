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
            print(f"os ingredientes do seu cachorro quente são: {self.ingrediente1}, {self.ingrediente2} é {self.ingrediente3}")

ingrediente1 = input("insira os tres ingredientes que deseja adicionar ao seu cachorro quente: ")
ingrediente2 = input("insira os tres ingredientes que deseja adicionar ao seu cachorro quente: ")
ingrediente3 = input("insira os tres ingredientes que deseja adicionar ao seu cachorro quente: ")



ingrediente = Cachorro_Quente(ingrediente1,ingrediente2,ingrediente3  )

ingrediente.apresentar()

#Herança
class Animal:
    def __init__(self,nome):
        self.nome = nome
        
    def emitir_som(self):
        print(f"{self.nome} diz: barulho")

class Cachorro(Animal): #herdando da classe animal
    pass
class Gato(Animal): #herdando da classe animal
    pass

dog = Cachorro("Rex") #dog é um objeto(instancia)
cat = Gato("Tom")

dog.emitir_som() #a instancia objeto esta herdando um metodo da classe pai
cat.emitir_som()

class Jogo:
    def __init__(self,nome,genero):
        self.nome = nome
        self.genero = genero
        
    def anuncio(self):
        print(f"O genero do jogo {self.nome} é {self.genero} ")
          
class jogo1(Jogo):
    pass

class Jogo2(Jogo):
    pass

j1 = jogo1("Hades", "ação")
j2 = Jogo2("outlast", "terror")

j1.anuncio()
j2.anuncio()

#polimorfismo

class Animal:
    def fazer_som (self):
        pass #metodo abastrato

class Cachorro(Animal):
    def fazer_som(self):
        print("O cachorro faz: Au Au!")

class Gato(Animal):
    def fazer_som(self):
        print("O gato faz: Miau!")

animais = [Cachorro(), Gato()]
for animal in animais:
    animal.fazer_som()
    
#exemplo polimorfismo
class Jogo:
    def __init__(self,nome,genero):
        self.nome = nome
        self.genero = genero
        
    def anuncio(self):
        pass

class jogo1(Jogo):
    def anuncio(self):
        print(f"O genero do jogo {self.nome} é {self.genero} ")  

class jogo2(Jogo):
    def anuncio(self):
        print(f"O genero do jogo {self.nome} é {self.genero} ") 
      

jogos = [jogo1("Hades", "ação"), jogo2("outlast", "terror")]

for jogo in jogos:
    jogo.anuncio()
    
#encapsulamento
class Pessoas:
    def __init__(self,nome):
        self.__nome = nome
        
    @property #getters
    def nome(self):
        return self.__nome
    
    @nome.setter #setters 
    def nome(self, novo_nome):
        if isinstance(novo_nome, str) and novo_nome.strip():
            self.__nome = novo_nome
        else:
            print("Nome inválido.")
            
# #uso da classe
# pessoa = Pessoas("Marcelo")
# print(pessoa.nome)
# pessoa.nome = "Bob"
# print(pessoa.nome)
# pessoa.nome = ""

#exemplo 
class Pessoa:
    def __init__(self,nome,idade):
        self.__nome = nome #atributo privado
        self.__idade = idade #atributo privado
        
    @property
    def nome(self):
        return self.__nome
    @property
    def idade(self):
        return self.__idade
    
    def exibir_informações(self):
        print(f"Nome: {self.__nome}, Idade: {self.__idade}")
        
pessoas = Pessoa("Alice", 30)
#tentativa de acessar o atributo privado __nome
print(pessoas.nome)
print(pessoas.idade)
pessoas.exibir_informações()