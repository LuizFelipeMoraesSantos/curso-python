import requests
import openpyxl

#url da API
url = "https://jsonplaceholder.typicode.com/users"

#fazendo a requisição de GET para a API

response = requests.get(url)

print(response)
#verificando os status da requisição
if response.status_code == 200:
    users = response.json() #convertendo a resposta em formato JSON
    
    for user in users:
        if user['name'] == "Leanne Graham": #buscando os dados com base o nome do usuario
            print(f"Nome: {user['name']}, Email: {user['email']},")#imprimindo os valores
            print(f"Telefone: {user['phone']}, Endereço: {user['address']}")
            
else:
    print(f"Falha ao obter dados. Status code: {response.status_code}")        

