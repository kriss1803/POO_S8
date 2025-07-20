# sistema_reservas_hotel.py

# Modelamos un sistema de reservas de hotel utilizando POO

# Clase Cliente representa a una persona que realiza una reserva
class Cliente:
    def __init__(self, nombre, correo):
        self.nombre = nombre
        self.correo = correo

    def __str__(self):
        return f"Cliente: {self.nombre}, Email: {self.correo}"


# Clase Habitacion representa una habitación del hotel
class Habitacion:
    def __init__(self, numero, tipo, precio):
        self.numero = numero
        self.tipo = tipo  # Simple, Doble, Suite
        self.precio = precio
        self.ocupada = False

    def ocupar(self):
        self.ocupada = True

    def liberar(self):
        self.ocupada = False

    def __str__(self):
        estado = "Ocupada" if self.ocupada else "Disponible"
        return f"Habitación {self.numero} ({self.tipo}) - {estado} - ${self.precio}"


# Clase Reserva representa la reserva hecha por un cliente
class Reserva:
    def __init__(self, cliente, habitacion, noches):
        self.cliente = cliente
        self.habitacion = habitacion
        self.noches = noches
        self.total = self.calcular_total()

    def calcular_total(self):
        return self.habitacion.precio * self.noches

    def confirmar(self):
        if not self.habitacion.ocupada:
            self.habitacion.ocupar()
            print(f"Reserva confirmada para {self.cliente.nombre} en habitación {self.habitacion.numero}. Total: ${self.total}")
        else:
            print(f"No se puede reservar la habitación {self.habitacion.numero}, ya está ocupada.")

    def __str__(self):
        return f"Reserva: {self.cliente.nombre} - Habitación {self.habitacion.numero} - {self.noches} noches - Total: ${self.total}"


# Bloque principal
if __name__ == "__main__":
    # Se crean clientes
    cliente1 = Cliente("Christian Peña", "cg.penar@uea.edu.ec")
    cliente2 = Cliente("Maria Martinez", "mmartinez@gmail.com")

    # Se crean habitaciones
    habitacion1 = Habitacion(101, "Simple", 50)
    habitacion2 = Habitacion(102, "Doble", 80)

    # Mostrar habitaciones
    print(habitacion1)
    print(habitacion2)

    # Crear y confirmar reservas
    reserva1 = Reserva(cliente1, habitacion1, 3)
    reserva1.confirmar()

    # Intentar reservar la misma habitación ocupada
    reserva2 = Reserva(cliente2, habitacion1, 2)
    reserva2.confirmar()

    # Reservar una habitación disponible
    reserva3 = Reserva(cliente2, habitacion2, 1)
    reserva3.confirmar()

    # Mostrar estados finales
    print(habitacion1)
    print(habitacion2)

