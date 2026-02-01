import random

class IndustrialError(Exception):
    def __init__(self, mensaje, id_dispositivo, codigo_error):
        super().__init__(mensaje)
        self.id_dispositivo = id_dispositivo
        self.codigo_error = codigo_error

class UmbralCritico(IndustrialError): pass
class SensorOffline(IndustrialError): pass
class ProductoAtascado(IndustrialError): pass

class Sensor:
    def __init__(self, id_sensor):
        self.id_sensor = id_sensor

    def leer(self, prob_falla, temp_max):
        if random.random() < prob_falla:
            raise SensorOffline("ERROR: Pérdida de señal MQTT", self.id_sensor, "E-404")
        
        temp = random.uniform(800, 1400)
        if temp > temp_max:
            raise UmbralCritico(f"CRÍTICO: {temp:.1f}°C", self.id_sensor, "E-911")
        return temp

class LineaProduccion:
    @staticmethod
    def verificar_atasco(prob):
        if random.random() < prob:
            raise ProductoAtascado("¡SISTEMA BLOQUEADO! Varilla obstruida en rieles.", "MEC-01", "JAM-STOP")