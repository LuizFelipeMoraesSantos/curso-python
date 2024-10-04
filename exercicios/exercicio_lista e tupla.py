#lista
lista = ["maçã","banana","laranja"]

#adicionando uva a lista
lista.append("uva")
print("Uva adicionada: ",lista)

#removendo banana
lista.remove("banana")
print("Banana Removida: ", lista)

#acessar e imprimir o segundo elemento da lista
acessar = lista.index("laranja")
print("o segundo elemento da lista é: ",lista[1])

#invertendo a ordem da lista
lista.reverse()
print("Lista invertida",lista)

#<--------------------------------------------->
#tuplas

Tupla = ("vermelho","verde","azul")
#desestruturando a tupla
a,b,c = Tupla
print(f"o primeiro elemento da tupla é {a} é o segundo é {c}")

#não é possivel adicionar outro elemento na tupla pois a tupla é imutavel
# Tupla.insert(1, "amarelo")
# print(Tupla)

#concatenação de tupla
tupla1 = ("amarelo","Roxo")
tupla3 = Tupla + tupla1
print(tupla3)

#desempacotamento de tupla
cor1,cor2,cor3 = Tupla
print(f"{cor1},{cor2},{cor3}")
 
#acessando o primero e ultimo elemento da tupla
print(Tupla[0],Tupla[2])