import openpyxl.workbook
import requests
import openpyxl

#url da API
url = "https://loteriascaixa-api.herokuapp.com/api/maismilionaria"

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
    sheet.append(["loteria","concurso","data","local","dezenasOrdemSorteio","dezenas","trevos","timeCoracao","mesSorte","premiacoes","estadosPremiados","observacao","acumulou","proximoConcurso","dataProximoConcurso","localGanhadores","valorArrecadado","valorAcumuladoConcurso_0_5","valorAcumuladoConcursoEspecial","valorAcumuladoProximoConcurso","valorEstimadoProximoConcurso"])
    
    #adicionando dados da API ao Excel
    for user in users:
        sheet.append([user['loteria'],user['concurso'],user['data'], user['local'],user['dezenasOrdemSorteio'],user['dezenas'],user['trevos'],user['timeCoracao'],user['mesSorte'],user['premiacoes']['descricao'],user['premiacoes']['faixa'],user['local'][ganhadores],user['local'][valorPremio],user['local']user['local']user['local']user['local']user['local']user['local']user['local']user['local']])
        
    #salvando o arquivo
    workbook.save("Mega_Sena.xlsx")
    print("Dados salvos no arquivo 'usuarios_api.xlsx' com sucesso.")
    
else:
    print(f"falha ao obter dados. status code: {response.status_code}")
    
