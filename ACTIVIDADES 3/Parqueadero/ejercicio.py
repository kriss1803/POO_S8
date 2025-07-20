class ConexionBaseDeDatos:
    """
    Clase que simula una conexión a una base de datos.
    Usa __init__ para establecer la conexión y __del__ para cerrarla automáticamente.
    """

    def __init__(self, nombre_bd):

        #Inicializa la conexión (simulada).
        self.nombre_bd = nombre_bd
        self.conectado = False
        self.conectar()

    def conectar(self):

        #Método que simula establecer una conexión a la base de datos.

        # Simulamos una conexión establecida
        self.conectado = True
        print(f"Conectado a la base de datos '{self.nombre_bd}'.")

    def ejecutar_consulta(self, consulta):

        #Método que simula la ejecución de una consulta SQL.

        if self.conectado:
            print(f"Ejecutando consulta en '{self.nombre_bd}': {consulta}")
        else:
            print("No se puede ejecutar la consulta. No hay conexión activa.")

    def cerrar_conexion(self):

        #Método que simula cerrar la conexión a la base de datos.

        if self.conectado:
            self.conectado = False
            print(f"Conexión con la base de datos '{self.nombre_bd}' cerrada manualmente.")

    def __del__(self):
        """
        Destructor que se llama automáticamente al destruir el objeto.
        Cierra la conexión si aún está activa.
        """
        if self.conectado:
            print(f"Destructor: cerrando conexión con la base de datos '{self.nombre_bd}'.")
            self.cerrar_conexion()


# Uso del programa
def main():
    print("Inicio del programa.")

    # Crea la instancia
    conexion = ConexionBaseDeDatos("clientes_db")

    conexion.ejecutar_consulta("SELECT * FROM clientes;")

    print("Fin del programa. El objeto se eliminará y se cerrará la conexión automáticamente.")


if __name__ == "__main__":
    main()
