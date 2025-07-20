class Vehiculo:
    def __init__(self, placa):
        self.placa = placa
        print(f"Vehículo con placa {self.placa} ha ingresado al parqueadero.")

    def __del__(self):
        print(f"Vehículo con placa {self.placa} ha salido del parqueadero.")


print("Iniciando simulación del parqueadero")

vehiculo1 = Vehiculo("PCD0569")
vehiculo2 = Vehiculo("PBX3202")
