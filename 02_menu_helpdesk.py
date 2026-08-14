def pedir_opcion():
    print("\n" + "="*30)
    print("      MENÚ DE HELPDESK")
    print("="*30)
    print("1. Registrar ticket")
    print("2. Listar tickets")
    print("3. Buscar por solicitante")
    print("4. Mostrar resumen por prioridad")
    print("5. Salir")
    return input("Seleccione una opción (1-5): ")

def registrar_ticket(tickets):
    solicitante = input("Ingrese el nombre del solicitante: ")
    asunto = input("Ingrese el asunto o problema: ")
    prioridad = input("Ingrese la prioridad (Alta/Media/Baja): ")
    
    # Se agrega el registro a la lista de diccionarios usando append()
    tickets.append({
        "solicitante": solicitante,
        "asunto": asunto,
        "prioridad": prioridad
    })
    print("Ticket registrado exitosamente.")

