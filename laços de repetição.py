# a sintaxe basica de um for em Python é:

# for variavel in sequencia:
#     bloco de codigo a ser executado

# exemplo1:

frutas = ["Maçã", "banana", "laranja"]

for i in frutas:
    print(frutas)
    
# A função range() gera uma seguencia de números, que é frequentemente utilizadas para laços for:

for i in range(5): #gera uma seguencia de 0 a 4
    print(i+1) # ele sempre começa do 0 mas caso eu queira começar do 1 eu faço 'i+1'
    
# o range(5) gera números de 0 a 4 (o último número não e incluído).

# exemplo2:

soma = 0 #contador

for i in range(1, 11):
    soma += i
    a = 0
    b = 10
    print(a)
    print(f"A soma de 1 a 10 é: {soma}")
    
print(f"A soma de 1 a 10 é: {soma}")
print(a)
    
    
# exempo3:

palavra ="Python"

for letra in palavra: 
    
    print(letra) #nesse caso, a variável assume cada caractere de string palavra 
    
    
for letra in palavra:
    i = palavra.index(letra)
    print(f"a letra {letra} tem indice {i}") #printando cada letra e mostrando indice
    

# exemplo4:

frase = input("Digite uma frase: ").lower()
vogais = "aeiou"
consoantes = "bcdfgjklmnpqrstvwxyez"
contador_vogal = 0
contador_consoante = 0

for letra in frase: #interando cada letra com frase
    if letra in vogais: #se tiver letras em vogais ele adiciona mais 1 no contador
        contador_vogal += 1

    elif letra in consoantes:
        contador_consoante += 1
print(f"Há {contador_vogal} vogais na frase")
print(f"Há {contador_consoante} consoantes na frase")
        

