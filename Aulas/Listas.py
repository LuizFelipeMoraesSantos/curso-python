lista1 = [] #uma lista vazia

lista1 = ["1","2","3"] #adicionando itens a uma lista
# print(type(lista1), lista1) #verificando o tipo da lista

# declaração explicita de lista
lista2 = list((1,"2",3))
# print(lista2)

#declaração implicita
lista3 = ["c",4.65, True, "True","Vamos Aprender", ["outra","lista","interna"], lista2]
# print(lista3)

lista4 = ["primeiro","segundo","terceiro"]
# print(lista4)

# acessando um elemento da lista
print(lista3)
print(lista3[4][2])
print(lista3[2:6:2])
print(lista3[:3])
print(lista3[-1:])
print("imprimindo de dois em dois", lista3[::2])
print(len(lista3))

lista1.append("python") #adicionando elemento a uma lista
# print(lista1)

lista1.insert(2,"c++") #substituindo o elemento de uma lista por outro


lista1[2] = "php" #substituindo um elemento de uma lista


indice = lista1.index("php") #puxando o index de um elmento especifico da lista


lista1[indice] = "css" #subustituindo um elemento por outro utilizando a variavel indice

print(lista1)


print("Lista original: ",lista1) 

#invertendo a lista
lista1.reverse()
print("Lista invertida: ", lista1)


lista1.sort()
print("lista Ordenada: ", lista1)


