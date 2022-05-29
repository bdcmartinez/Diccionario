import json
import random

# 0 = Español
# 1 = English

idioma = 1

with open("diccionario.json") as jsonfile:
    lista = json.load(jsonfile)
    dic = lista[idioma]

pasw = list(dic.keys())

for i in range(len(pasw)):
    a = dic[pasw[i]]
    dic[pasw[i]] = [a,0]

lista[idioma] = dic
        
with open("diccionario.json","w") as jsonfile:
    json.dump(lista,jsonfile)
