print("Proporcione los siguientes datos del libro: ")
nombre = input("Proporciona el nombre: ")
id = int(input("Proporcione el ID: "))
precio = float(input("Proporcione el Precio: "))
envioGratuito = input("Indica si el envio es gratuito (True/False): ")

if envioGratuito == "True":
    envioGratuito = True
elif envioGratuito == "False":
    envioGratuito = False
else:
    envioGratuito = "Valor incorrecto, debe ser True/False"

print("Nombre: ", nombre)
print("Id: ", id)
print("Precio: ", precio)
print("Evio Gratuito?: ", envioGratuito)
print(type(envioGratuito))