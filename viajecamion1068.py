print("Cesar Gerardo Jaramillo Najera 1068")
print("Central de camiones, viajes")

class viajes1068:
    id_viaje=0
    Origen=""
    Destino=""
    Horario=""
    Distanciarecorrida=""
    Paradasintermedias=0
    Costo=0

    def mostrardatos(self):
        print("-----------------MOSTRAR DATOS-------------------------------------------")
        print(f"El id del viaje es: {self.id_viaje}")
        print(f"El Origen (De donde sale) del viaje es: {self.Origen}")
        print(f"El Destino(Donde va a llegar) del viaje es: {self.Destino}")
        print(f"El horario que tiene el viaje es: {self.Horario}")
        print(f"La distancia que recorrera el viaje es: {self.Distanciarecorrida}")
        print(f"La cantidad de paradas intermedias sera de: {self.Paradasintermedias}")
        print(f"El costo del viaje sera: {self.Costo}")
        print("------------------------------------------------------------------------")
    
    def lista_viajes(self):
        print("---------------------------------------------------")
        print("LISTA DE DESTINOS DE VIAJES")
        destinos = ["Chihuahua", "Delicias", "Casas Grandes"]
        for disponibles in destinos:
            print(disponibles)
    
    def tupla_costos(self):
        print("---------------------------------------------------")
        print("TUPLA DE COSTOS DE LOS VIAJES")
        precio = ("$2,200","$2,800", "$3,000")
        for costo in precio:
            print(costo)
    def viaje_horario(self):
        print("---------------------------------------------------")
        print("HORARIOS DE LOS VIAJES (DICCIONARIO)")
        viajar = {
            "Chihuahua": "12:00PM-7:00PM",
            "Delicias":  "8:00AM-2:00PM",
            "Casas Grandes": "6:00PM-11:00PM"
        }
        for x, y in viajar.items():
            print(x,y)
    
    def sisepudo1068(self):
        print("El pasajero si pudo hacer su viaje que agusto se ve")

    def nosepudo1068(self):
        print("El pasajero no pudo hacer su viaje que triste se ve")

datos=viajes1068()
datos.id_viaje= 1
datos.Origen="Cd. Juarez"
datos.Destino="Chihuahua","Delicias","Casas Grandes"
datos.Horario="12-00PM-7:00PM","8:00AM-2:00PM","6:00PM-11:00PM"
datos.Distanciarecorrida="300km","450km","113Km"
datos.Paradasintermedias="3","2","1"
datos.Costo="$2,200","$2,800","$3,000"
datos.mostrardatos()
datos.lista_viajes()
datos.tupla_costos()
datos.viaje_horario()
datos.sisepudo1068()
datos.nosepudo1068()