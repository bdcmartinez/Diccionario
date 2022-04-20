import json




with open("diccionario.json") as jsonfile:
    lista = json.load(jsonfile)
    dic = lista[0]

    
    
while True:
    palabra = input("¿Qué palabra desea agregar? ")
    definicion = input("¿Que significado tiene la palabra?")

    if palabra == "c":
        break
    else:
        dic[palabra] = definicion


lista = [dic]
        
with open("diccionario.json","w") as jsonfile:
    json.dump(lista,jsonfile)


with open("diccionario.json") as jsonfile:
    lista = json.load(jsonfile)
    dic = lista[0]
    print(dic)