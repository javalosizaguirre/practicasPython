nombres = ["Juan", "Karla", "Ricardo", "Maria"]
print(nombres)

# Conocer el largo de la lista
print(len(nombres))
print(nombres[0])

# navegacion inversa
print(nombres[-1])


# imprimir rango
print(nombres[0:2])

# Imprimir los elementos de inicio hasta el indice proporcionado
print(nombres[:2])

# Imprmir los elementos hasta el final desde el indice proporcionado
print(nombres[1:])

# Cambiar los elementos de una lista
nombres[3] = "Ivone"

print(nombres)


# iterando lista

for nom in nombres:
    print(nom)

# Revisar si existe un elemento en la lista

if "Karla" in nombres:
    print("Karla si existe en nuestra lista")
else:
    print("El elemento buscado no existe en nuestra lista")

# Agregando un nuevo elemento
nombres.append("Lorenzo")

print(nombres)

# Insertar elemento en el indice proporcionado
nombres.insert(1, "Octavio")
print(nombres)

# Remover elementos

nombres.remove("Octavio")
print(nombres)

# Remover el ultimo elemento de la lista
nombres.pop()
print(nombres)

#Remover el indice indicado de la lista

del nombres[0]
print(nombres)

#limpiar los elementos de nuestra lista

nombres.clear()
print(nombres)

#eliminar por completo la lista

del nombres
print(nombres)