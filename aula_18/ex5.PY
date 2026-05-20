# 5) Elaborar um programa para inverter o dicionário, trocando suas chaves e valores, de forma que cada valor 
# riginal se torne uma chave e cada chave original se torne o valor correspondente. Exibir o novo dicionário. 

dados = {
    "nome": "Sandro",
    "idade": 30,
    "cidade":"Sao Paulo",
    "estado":"Sao Paulo"

}

dados_n = {

}


for chave, valor in dados.items():
    dados_n[valor] = chave

    print(dados_n) 
       
