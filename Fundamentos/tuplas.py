# Tupla mantiene el orden, perso ya no se puede
frutas = ("Naranja", "Platano", "Guayaba")
print(frutas)

# largo de las tuplas
print(len(frutas))

# accediendo a un elemento
print(frutas[2])

# Navegacion inversa

print(frutas[-1])

# rango
print(frutas[0:2])

# modificar un valor
#frutas[0] = "Naranjita"
frutasLista = list(frutas)
frutasLista[1] = "Platanito"
frutas = tuple(frutasLista)
print(frutas)

for fruta in frutas:
    print(fruta)
