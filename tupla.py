tupla1 = (1,2,3)
tupla2 = ("quatro", "cinco")
tupla3 = tupla1 + tupla2
print(tupla3) #output (1, 2, 3, 'quatro', 'cinco') 


#desestruturação de tupla
tupla =(1,2,3)
a,b,c = tupla
print(a) #output 1
print(b) #output 2
print(c) #output 3

#verificação de dados na tupla
tuplas = (1,2,3)
print(2 in tuplas) #output True
print(4 in tupla) #output False

#count

contar = (1,2,3,1,2,3,1,3)
print(contar.count(2)) #output 2
print(contar.count(4)) #output 0

str = "Marca"
print(str.count("a"))