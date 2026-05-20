dicionario = {
    "123": "vsf",
    "321": "fsv"
}

dicionario.pop()
dicionario.clear()
dicionario.copy()

dicionario.get() 

'''
rgm = {“Liz”: 229874, “Hugo”: 215793, “Sofia”:
199745}
print(rgm.get(“Hugo”))
#215793
print(rgm.get(“Sandro”))
#None
print(rgm.get(“Maria”,“Nãoexiste”))
#Nãoexiste
'''

dicionario.items() #retorna todos os pares chave/conteudo do dicionario
dicionario.update() #atualiza ou mescla com outro dicionario
dicionario.values() #retorna todos os valores do dicionario
dicionario.keys() #retorna todas as chaves do dicionario
