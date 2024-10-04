escola = {"nome": "Marcelo", "Idade": 17, "nota": 7.5}

escola["curso"] = "Ciência da computação"
print(f"curso adicionado no dicionario {escola}")
 
nome_aluno = escola.get("nome")
print(nome_aluno)

del escola["nota"]
print(escola)

print("Idade" in escola)