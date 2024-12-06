class Pessoa:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
pessoa1 = Pessoa("Guilherme", 17 )
print(pessoa1.nome)
print(pessoa1.idade)

class Carro:
    def __init__(self,marca,modelo,ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    
    def descricao(self):
        print(f"A marca do seu carro é: {self.marca}, o modelo é: {self.modelo}, e o ano é: {self.ano}")
        
especificacao =Carro("volkswagen", "Fusca", 1962)
especificacao.descricao()

class Livro:
    def __init__(self, titulo, autor, numero_pagina, pagina):
        self.titulo = titulo
        self.autor = autor
        self.numero_paginas = numero_pagina
        self.pagina = pagina
    def ler_pagina(self):
        print(f"Voçê está lendo a página {self.pagina} do livro")

livros = Livro("Hábitos Atômicos", "Jamoes Clear", 288, 20)
livros.ler_pagina()

class Retangulo:
    def __init__(self, altura, largura):
        self.altura = altura
        self.largura = largura
        self.mult = altura*largura
    def calculo(self):
        print(f"Um retângulo de altura de: {self.altura}, e {self.largura} de largura é igual a: {self.mult}")
        
retangulos = Retangulo(12, 32)
retangulos.calculo()

class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
    
        
        
        


        
        
    