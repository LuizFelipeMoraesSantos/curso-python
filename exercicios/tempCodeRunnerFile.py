frase = "Python é divertido!"
palavras = frase.split()
juntas = ''.join(palavras)
letras = 0

for letra in juntas:
    letras += 1
print(letras)