class MiClase:
    variable_clase = "Variable de clase"

    def __init__(self, variable_instancia):
        self.variable_instancia = variable_instancia


print(MiClase.variable_clase)

objeto1 = MiClase("Variable Instancia")
MiClase.variable_instancia = "Modificando variable de instancia"
print(MiClase.variable_instancia)
print(objeto1.variable_instancia)

# Podemos accerder a las variables de clase desde los objetos
print(objeto1.variable_clase)

# Podemos accerder a las variables con el nombre de la clase
print(MiClase.variable_clase)
