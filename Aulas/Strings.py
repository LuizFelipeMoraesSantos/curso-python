#declarando uma string
mensagem = "hellou, world!"

#concatenando strings

primeiro_nome = "Marcelo"
sobrenome = "Rocha"
nome_completo = primeiro_nome + " " +sobrenome #utilizando (" ") no meio da concatenação para os strings não ficarem colados 

print(nome_completo)

#Acessando caracteres individuais em uma string:

mensagem = "hellou, world!"
primeiro_caractere = mensagem[0] #acessando a primeira letra da string utilizando o index 0 #output 'h'
ultimo_caractere = mensagem[-1] #acessando a ultima letra da string utilizando o -1 que mostra o ultimo indice #output '!'

#encontrando o comprimento de uma string:

mensagem =  "Hello, world!"
comprimento = len(mensagem) #O len conta quantos elementos tem em uma string
print(comprimento) #output 13

#convertendo uma string para letra maiúscula ou minuscula
maiuscula = mensagem.upper()
minuscula = mensagem.lower()
#Convertendo um caractere especifico 
mensagem = "Hello, world!"
primeira_linha = mensagem[2:] #cortando a string ate 'ello, world!'
H = mensagem[0] #puxando o caractere 'H'
E = mensagem[1] #puxando o caractere 'E'
maiusculo = E.upper() #transformando o 'E' maisculo
minusculo = H.lower() #transformando o 'H' minusculo porque na variavel ele ta maiusculo

juncao = minusculo + maiusculo + primeira_linha #concatenando tudo

print(juncao)

#removendo espaços em branco de uma string:
frase ="   hello, world!   "
sem_espaços = frase.strip()# retorna "Hello, world!"
print(sem_espaços)
