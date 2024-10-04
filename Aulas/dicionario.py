dic = {} #criando um dicionario vazio
print(type(dic)) #verificando se a variavel 'Dic' é realmente um dicionario
dic_pernambuco = {"Sport": 41,"Santa Cruz": 29, "Nautico": 21} #criando um dicionario ja com chaves é valores 
print(dic_pernambuco)

#adicionando um elemento no dicionario (chave: valor)
# onde a chave é "salgueiro" é o valor é 1
# note que a chave é passada dentro de colchetes, após o nome do dicionario.
dic_pernambuco["Salgueiro"] = 1
print("adicionando 'Salgueiro' no dicionario: ",dic_pernambuco)

#buscando o valor com base na chave
qnt_titulos = dic_pernambuco.get("Sport") #acessando o valor com base na chave "Sport"
print(qnt_titulos)
print(f"o Sport tem {qnt_titulos} titulos")

#Removendo um valor com base na chave
del dic_pernambuco["Salgueiro"] #utilizando o del remove eternamente a chave é o valor
print(dic_pernambuco)

#Remove a chave e retorna seu valor
valor = dic_pernambuco.pop("Nautico") #diferente do (del) o pop exclui e armazena o valor da chave
print(f"O valor retornado da chave é: {valor}")
print(dic_pernambuco)

#verificando se uma chave existe no dicionario
print("Santa Cruz" in dic_pernambuco)

#pegar todas as chaves do dicionario
chaves = (dic_pernambuco.keys()) #retorna uma lista dentro de uma tupla
print(chaves)

acessar = list(chaves) #transformando em uma lista
print(acessar[0]) #acessando um elemento especifico

#pegar todos os valores do dicionario
teste = dic_pernambuco.values()

dic_paulista = {"Corinthias": 29, "Santos": 22, "Palmeiras": 22}

#Removendo e retornando o ultimo elemento
print(dic_paulista.popitem()) #ele apaga e retonorna o ultimo elemento do dicionario
print(dic_paulista)

#mesclar dois dicionarios
dic_pernambuco.update(dic_paulista) #ele junta dois dicionarios em um so (ele mescla com a variavel inserida a esquerda)
print(dic_pernambuco)

#Convertendo um dicionario em uma lista 
print(list(dic_pernambuco)) #transformando um dicionario em uma lista
print(list(dic_pernambuco.values())) #transformando um dicionario em uma lista é retornando so os valores





