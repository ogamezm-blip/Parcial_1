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

def listar_tickets(tickets):
    # Uso de len() para verificar si hay tickets
    if len(tickets) == 0:
        print("No hay tickets registrados en memoria.")
    else:
        print("\n--- Lista de Tickets ---")
        for i in range(len(tickets)):
            t = tickets[i]
            print(f"[{i+1}] Solicitante: {t['solicitante']} | Prioridad: {t['prioridad']} | Asunto: {t['asunto']}")

def buscar_por_solicitante(tickets):
    busqueda = input("Ingrese el nombre del solicitante a buscar: ")
    encontrados = 0
    
    print(f"\n--- Resultados para '{busqueda}' ---")
    for t in tickets:
        # Comparación sin distinguir mayúsculas/minúsculas usando .lower()
        if t["solicitante"].lower() == busqueda.lower():
            print(f"-> Prioridad: {t['prioridad']} | Asunto: {t['asunto']}")
            encontrados += 1
            
    if encontrados == 0:
        print("No se encontraron tickets para ese solicitante.")

def mostrar_resumen(tickets):
    # Contadores para el resumen
    alta, media, baja = 0, 0, 0
    
    for t in tickets:
        prioridad = t["prioridad"].lower()
        if prioridad == "alta":
            alta += 1
        elif prioridad == "media":
            media += 1
        elif prioridad == "baja":
            baja += 1
            
    print("\n--- Resumen por Prioridad ---")
    print(f"Alta:  {alta}")
    print(f"Media: {media}")
    print(f"Baja:  {baja}")
    # Uso de len() para el total
    print(f"Total de tickets en memoria: {len(tickets)}")

def ejecutar_menu():
    # Lista que mantendrá los tickets durante la ejecución
    tickets = [] 
    
    # Uso del bucle while para mantener el menú activo
    while True:
        opcion = pedir_opcion()
        
        # Estructura if/elif/else para controlar el flujo del menú
        if opcion == '1':
            registrar_ticket(tickets)
        elif opcion == '2':
            listar_tickets(tickets)
        elif opcion == '3':
            buscar_por_solicitante(tickets)
        elif opcion == '4':
            mostrar_resumen(tickets)
        elif opcion == '5':
            print("Saliendo del sistema Helpdesk. ¡Hasta pronto!")
            break
        else:
            print("Opción inválida. Por favor, intente de nuevo.")

# Condición para iniciar el menú
if __name__ == "__main__":
    ejecutar_menu()
