import openpyxl.workbook
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
    
    #criando um novo arquivo Excel
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    
    #adicionando os cabeçalhos
    sheet.append(["ID","Nome","Email","Empresa"])
    
    #adicionando dados da API ao Excel
    for user in users:
        sheet.append([user['id'],user['name'],user['email'], user['company']['name']])
        
    #salvando o arquivo
    workbook.save("usuarios_api.xlsx")
    print("Dados salvos no arquivo 'usuarios_api.xlsx' com sucesso.")
    
else:
    print(f"falha ao obter dados. status code: {response.status_code}")
    
