# Un diccionario esta compuesto de llave valor (key,value)
diccionario = {
    "IDE": "Integrated Development Envirenment",
    "OOP": "Object Oriented Programming",
    "DBMS": "Database Managment Sysrtem"
}

print(diccionario)
print(len(diccionario))

# Accediendo a un elemento
print(diccionario["IDE"])
print(diccionario.get("OOP"))


# Modificando valores
diccionario["IDE"] = "Integrated development envirenment"
print(diccionario)

for termino  in diccionario:
    print(diccionario[termino])
    
    
for valor in diccionario.values():
    print(valor)