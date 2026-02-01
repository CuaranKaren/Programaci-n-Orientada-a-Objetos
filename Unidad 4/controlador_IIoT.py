import time
from modelo import Sensor, LineaProduccion, UmbralCritico, SensorOffline, ProductoAtascado
from vista import MonitorVista

class PlantaController:
    def __init__(self, config):
        self.v = MonitorVista()
        self.conf = config
        self.sensores = {
            "1": [Sensor("LAM-01"), Sensor("LAM-02")],
            "2": [Sensor("VAR-01"), Sensor("VAR-02")]
        }

    def iniciar_monitoreo(self):
        while True:
            opcion = self.v.menu_principal()
            if opcion == "3": break
            if opcion not in self.sensores: continue

            print(f"\nIniciando Monitoreo Sección {opcion} ")
            
            try:
                while True:
                    for s in self.sensores[opcion]:
                        try:
                            val = s.leer(self.conf['prob_falla'], self.conf['temp_max'])
                            self.v.mostrar_lectura(s.id_sensor, val)
                        except (UmbralCritico, SensorOffline) as e:
                            self.v.alerta_emergencia(e)
                    
                    LineaProduccion.verificar_atasco(self.conf['prob_atasco'])
                    
                    time.sleep(1.5) 
            
            except ProductoAtascado as e:
                self.v.alerta_emergencia(e)
                while True:
                    entrada = self.v.pedir_reinicio()
                    if entrada == "reiniciar":
                        print("\nLiberando mecánicamente... Sistema Listo.")
                        break
                    else:
                        print(f"ERROR: No se puede iniciar sin comando de seguridad.")
            
            except KeyboardInterrupt:
                print("\n>> Volviendo al menú principal...")