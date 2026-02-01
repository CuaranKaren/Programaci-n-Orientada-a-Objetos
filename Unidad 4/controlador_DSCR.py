from modelo import SensorAmbiente, Actuador

class Controlador:
    def __init__(self, vista):
        self.vista = vista
        self.sensor = SensorAmbiente(4) 
        self.vent = Actuador(17, "Verde") 
        self.calef = Actuador(27, "Rojo") 
        self.falla = Actuador(22, "Azul") 
        self.modo_manual = False

    def cambiar_modo(self):
        self.modo_manual = not self.modo_manual

    def toggle_v(self):
        if self.modo_manual: self.vent.gestionar(not self.vent.estado)

    def toggle_c(self):
        if self.modo_manual: self.calef.gestionar(not self.calef.estado)

    def ciclo(self):
        try:
            t, h = self.sensor.leer()
            self.falla.gestionar(False) # Si lee bien, apaga LED azul
            
            if not self.modo_manual:
                v_on = t > 28
                c_on = t < 18
                self.vent.gestionar(v_on)
                self.calef.gestionar(c_on)
            
            self.vista.actualizar(t, h, self.modo_manual, self.vent.estado, self.calef.estado, False)

        except AssertionError as e:
            # ESTA PARTE ENCIENDE EL LED AZUL
            print(f"BLOQUEO POR ASSERTION: {e}")
            self.falla.gestionar(True)
            self.vista.actualizar(0, 0, self.modo_manual, False, False, True)
            self.vista.popup_error(str(e))
            return # Detener ciclo por seguridad

        except Exception as e:
            print(f"Error temporal: {e}")

        self.vista.after(2000, self.ciclo)
