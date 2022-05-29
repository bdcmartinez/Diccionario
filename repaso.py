from html.entities import name2codepoint
from pprint import pprint
import random
import json

# 0 = Español
# 1 = English

idioma = 1


with open("diccionario.json") as jsonfile:
    lista = json.load(jsonfile)
    dic = lista[idioma]
pasw = list(dic.keys())


print("*Bienvenido al repaso*")
while True:

    c = input()
    if c == "":
        n = random.randint(0,len(pasw)-1)
        print(pasw[n]+"\n"+dic[pasw[n]][0])
        dic[pasw[n]][1] +=1
    else:
        break
    
    
    
    
lista[idioma] = dic
        
with open("diccionario.json","w") as jsonfile:
    json.dump(lista,jsonfile)


with open("diccionario.json") as jsonfile:
    lista = json.load(jsonfile)
    dic = lista[idioma]