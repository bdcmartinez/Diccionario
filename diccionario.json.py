import json

# 0 = Español
# 1 = English

idioma = 1

with open("diccionario.json") as jsonfile:
    lista = json.load(jsonfile)
    dic = lista[idioma]

while True:
    palabra = input("¿Qué palabra desea agregar? ")
    definicion = input("¿Que significado tiene la palabra? ")

    if palabra == "s":
        break
    else:
        dic[palabra] = definicion


lista[idioma] = dic
        
with open("diccionario.json","w") as jsonfile:
    json.dump(lista,jsonfile)


with open("diccionario.json") as jsonfile:
    lista = json.load(jsonfile)
    dic = lista[idioma]
    print(dic)