minha_lista = [76,92.3,"oi",True,4,76]
 
minha_lista.append("Pera")
minha_lista.append(75)
print("adicionando pera e 75 no final da lista",minha_lista)

minha_lista.insert(3 , "gato")
print("adicionando gato no index 3",minha_lista)

minha_lista.insert(0, 99)
print("adicionando 99 no começo da lista",minha_lista)

indice = minha_lista.index("oi")
print("index de 'oi' é: ",indice)

minha_lista.remove(True)
print("removendo True da lista",minha_lista)
