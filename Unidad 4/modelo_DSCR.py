import board
import adafruit_dht
import RPi.GPIO as GPIO

class SensorAmbiente:
    def __init__(self, pin_bus):
        # ASSERTION 1: Configuración de hardware (Verifica que el pin existe)
        assert hasattr(board, f"D{pin_bus}"), f"El pin GPIO {pin_bus} no es válido en board."
        self.sensor = adafruit_dht.DHT11(getattr(board, f"D{pin_bus}"))

    def leer(self):
        try:
            t = self.sensor.temperature
            h = self.sensor.humidity
            
            if t is None or h is None:
                raise RuntimeError("Datos incompletos")

            # ASSERTION 2: Integridad de Datos (Filtra lecturas basura)
            assert -5 <= h <= 10, f"Humedad fuera de rango: {h}%"
            assert -10 <= t <= 60, f"Temperatura fuera de rango: {t}°C"
            
            return t, h
        except RuntimeError as e:
            raise Exception(f"Sincronizando: {e}")

class Actuador:
    def __init__(self, pin, nombre):
        self.pin = pin
        self.nombre = nombre
        GPIO.setup(self.pin, GPIO.OUT)
        self.estado = False

    def gestionar(self, encender):
        # ASSERTION 3: Seguridad de Operación (Evita estados indefinidos)
        assert isinstance(encender, bool), "El estado debe ser booleano"
        GPIO.output(self.pin, GPIO.HIGH if encender else GPIO.LOW)
        self.estado = encender
