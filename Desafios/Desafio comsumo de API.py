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
        try:
            dezenasOrdemSorteio = ', '.join(user.get('dezenasOrdemSorteio', []))
            dezenas = ', '.join(user.get('dezenas', []))
            trevos = ', '.join(user.get('trevos',[]))
            
            estadosPremiados = user.get('estadosPremiados', [])
            estadosPremiados_str = ', '.join([str(i['local']) for i in  estadosPremiados if 'local' in i])
            
            localGanhadores = user.get('localGanhadores', [])
            localGanhadores_str = ', '.join([str(g['local']) for g in localGanhadores if 'local' in g])
            sheet.append([
                user['loteria'],
                user['concurso'],
                user['data'],
                user['local'],
                dezenasOrdemSorteio,
                dezenas,
                trevos,
                user['timeCoracao'],
                user['mesSorte'],
                user['premiacoes'][0]['descricao'],
                user['premiacoes'][0]['faixa'],
                user['premiacoes'][0]['ganhadores'],
                user['premiacoes'][0]["valorPremio"],
                estadosPremiados_str,
                user['observacao'],
                user['acumulou'],
                user['proximoConcurso'],
                user['dataProximoConcurso'],
                localGanhadores_str,
                user['valorArrecadado'],
                user['valorAcumuladoConcurso_0_5'],
                user['valorAcumuladoConcursoEspecial'],
                user['valorAcumuladoProximoConcurso'],
                user['valorEstimadoProximoConcurso']
            ])
        except KeyError as e:
            print(f"Chave ausente em user: {e}")
        
    #salvando o arquivo
    workbook.save("Mega_Sena.xlsx")
    print("Dados salvos no arquivo 'Mega_Sena.xlsx' com sucesso.")
    
else:
    print(f"falha ao obter dados. status code: {response.status_code}")
    
