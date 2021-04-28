class Persona:
    def __init__(self, nombre, ape_paterno, ape_materno):
        self.nombre = nombre  # Atributo Publico
        self._apellido_paterno = ape_paterno  # Atributo Protegido
        self.__apellido_materno = ape_materno  # Atributo privado

    def metodo_publico(self):
        self.__metodo_privado()

    def __metodo_privado(self):
        print(self.nombre)
        print(self._apellido_paterno)        

    def set_apellido_materno(self, apellido_materno):
        self.__apellido_materno = apellido_materno

    def get_apellido_materno(self):
        return self.__apellido_materno


p1 = Persona("Juan", "Lopez", "Perez")

p1.metodo_publico()

print(p1.nombre)
print(p1._apellido_paterno)
print(p1.get_apellido_materno())
