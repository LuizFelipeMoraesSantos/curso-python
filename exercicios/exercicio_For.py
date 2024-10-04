#exercicio 1

for i in range(1,11):
    print(i)
    
    
#exercicio 2
soma = 0
for i in range(1,51):
    soma +=i
    print(f"a soma de 1 a 50 é: {soma}")
    
#exercicio 3
tabuada = int(input("insira o numero que deseja saber a tabuada: "))
mult = 0
for numero in range(1,11):
    mult += 1
    print(f"{tabuada}x{mult} =",mult*tabuada)
    
#exercicio 4
pares = 0
for i in range(1,21):
    pares +=1
    if pares %2 ==0:
        print(i)
        
#exercicio 5
frase = "Python é divertido!"
palavras = frase.split()
juntas = ''.join(palavras)
letras = 0

for letra in juntas:
    letras += 1
print(letras)


#exercicio 6

lista = [1,2,3,4,5,6]

for i in lista:
    lista.reverse()
    print(lista)
    
#exercicio 7



#exercicio 8
cont = 0

for i in range(1,101):
    cont =+1
    print(i*i)
    


    
    
    
    
    