class MonitorVista:
    @staticmethod
    def menu_principal():
        print("\n" + "="*30)
        print(" SELECCIONE SECCIÓN A MONITOREAR")
        print(" 1. Sección Laminados (2 Sensores)")
        print(" 2. Sección Varilla (2 Sensores)")
        print(" 3. Salir")
        print("="*30)
        return input("Selección: ")

    @staticmethod
    def mostrar_lectura(id_s, valor):
        print(f" > [OK] {id_s}: {valor:.2f}°C")

    @staticmethod
    def alerta_emergencia(e):
        print(f"\n!!! {type(e).__name__} !!!")
        print(f"ID: {e.id_dispositivo} | MSG: {e}")

    @staticmethod
    def pedir_reinicio():
        print("\n" + "#"*40)
        print(" LÍNEA DETENIDA POR SEGURIDAD")
        print(" Escriba 'reiniciar' para liberar la máquina.")
        print("#"*40)
        return input(">> ").lower()