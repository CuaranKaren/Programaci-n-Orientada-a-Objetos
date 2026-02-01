import RPi.GPIO as GPIO
from vista import VistaDomotica
from controlador import Controlador

def main():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    # Configurar salidas: 17=Verde, 27=Rojo, 22=Azul
    GPIO.setup([17, 27, 22], GPIO.OUT)

    try:
        vista = VistaDomotica()
        controlador = Controlador(vista)
        vista.conectar(controlador)
        
        controlador.ciclo()
        vista.mainloop()
    finally:
        GPIO.cleanup()

if __name__ == "__main__":
    main()
