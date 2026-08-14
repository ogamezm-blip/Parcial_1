# 03_modelos.py

class Usuario:
    def __init__(self, id_usuario, nombre, email, rol):
        self.id = id_usuario
        self.nombre = nombre
        self.email = email
        self.rol = rol

    def __str__(self):
        return f"{self.nombre} (Rol: {self.rol})"


class Ticket:
    # Definimos los estados válidos como un atributo de la clase
    ESTADOS_VALIDOS = ["Open", "In Progress", "Resolved", "Closed", "Cancelled"]

    def __init__(self, id_ticket, titulo, categoria, prioridad, solicitante):
        self.id = id_ticket
        self.titulo = titulo
        self.categoria = categoria
        self.prioridad = prioridad
        self.solicitante = solicitante # Esto recibirá un objeto Usuario
        self.tecnico = None            # Opcional, inicia vacío
        self._status = "Open"          # Atributo protegido con _

    def cambiar_estado(self, nuevo_estado):
        """Modifica el estado validando que pertenezca a la lista permitida."""
        if nuevo_estado in self.ESTADOS_VALIDOS:
            self._status = nuevo_estado
            print(f"El estado del ticket #{self.id} ha cambiado a: '{self._status}'.")
        else:
            print(f"Error: '{nuevo_estado}' no es un estado válido.")

    def asignar_tecnico(self, tecnico):
        """Asigna un técnico validando su rol."""
        # Comparamos en minúsculas por seguridad
        if tecnico.rol.lower() == "technician":
            self.tecnico = tecnico
            print(f"Técnico {tecnico.nombre} asignado con éxito al ticket #{self.id}.")
        else:
            print(f"Error: El usuario {tecnico.nombre} no tiene permisos de técnico.")

    def __str__(self):
        # Operador ternario para mostrar "Sin asignar" si no hay técnico
        nombre_tecnico = self.tecnico.nombre if self.tecnico else "Sin asignar"
        
        return (f"Ticket #{self.id} | {self.titulo} | Estado: {self._status}\n"
                f"  -> Solicitante: {self.solicitante.nombre}\n"
                f"  -> Técnico: {nombre_tecnico}")


