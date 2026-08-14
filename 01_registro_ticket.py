# 01_registro_ticket.py

print("SISTEMA DE REGISTRO DE TICKETS")

while True:
    try:
        numero_ticket = int(input("Ingrese el número de ticket: "))
        break # Si es un número válido, rompemos el bucle y avanzamos
    except ValueError:
        print("Error: El número de ticket debe ser un valor numérico válido. Intente de nuevo.")

# Funcion para validar que los campos de texto no esten vacios
def pedir_campo_obligatorio(mensaje):
    while True:
        valor = input(mensaje).strip()
        if valor != "":
            return valor
        print("Error: Este campo es obligatorio y no puede estar vacío.")


solicitante = pedir_campo_obligatorio("Ingrese el nombre del solicitante: ")
titulo = pedir_campo_obligatorio("Ingrese el título del ticket: ")
descripcion = pedir_campo_obligatorio("Ingrese la descripción del problema: ")

# Solicitar y validar Categoría
categorias_validas = ["General", "Hardware", "Software", "Network"]
while True:
    categoria = input(f"Ingrese la categoría {categorias_validas}: ").capitalize()
    if categoria in categorias_validas:
        break
    print("Error: Categoría no válida. Debe ser una de las opciones listadas.")

