lista1 = [] #uma lista vazia

lista1 = [1,"2",3] #adicionando itens a uma lista
# print(type(lista1), lista1) #verificando o tipo da lista

# declaração explicita de lista
lista2 = list((1,"2",3))
# print(lista2)

#declaração implicita
lista3 = ["c",4.65, True, "True","Vamos Aprender", ["outra","lista","interna"], lista2]
# print(lista3)

lista4 = ["primeiro","segundo","terceiro"]
# print(lista4)

#acessando um elemento da lista
print(lista3)
print(lista3[4][2])