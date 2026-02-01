import tkinter as tk
from tkinter import messagebox

class VistaDomotica(tk.Tk):
    def __init__(self):
        super().__init__()
        self.controlador = None 
        self.title("Smart Home Monitor")
        self.geometry("400x550")
        self.configure(bg="#1a1a1a")

        # Pantalla de Temperatura
        self.lbl_temp = tk.Label(self, text="--°C", font=("Impact", 50), bg="#1a1a1a", fg="#00ff00")
        self.lbl_temp.pack(pady=20)
        
        self.lbl_hum = tk.Label(self, text="Humedad: --%", font=("Arial", 12), bg="#1a1a1a", fg="white")
        self.lbl_hum.pack()

        # Botón de Cambio de Modo
        self.btn_modo = tk.Button(self, text="AUTO", width=15, font=("Arial", 12, "bold"))
        self.btn_modo.pack(pady=20)

        # Controles Manuales
        self.frame_m = tk.LabelFrame(self, text=" Control Manual ", bg="#1a1a1a", fg="white", padx=10, pady=10)
        self.frame_m.pack(pady=10)
        self.btn_v = tk.Button(self.frame_m, text="VENT")
        self.btn_v.grid(row=0, column=0, padx=10)
        self.btn_c = tk.Button(self.frame_m, text="CALEF")
        self.btn_c.grid(row=0, column=1, padx=10)

        # Indicadores de estado (LEDs Virtuales)
        self.canvas = tk.Canvas(self, width=300, height=100, bg="#1a1a1a", highlightthickness=0)
        self.canvas.pack()
        self.ind_v = self.canvas.create_oval(30, 20, 70, 60, fill="gray") # Verde
        self.ind_c = self.canvas.create_oval(130, 20, 170, 60, fill="gray") # Rojo
        self.ind_f = self.canvas.create_oval(230, 20, 270, 60, fill="gray") # Azul (FALLO)

    def conectar(self, controlador):
        self.controlador = controlador
        self.btn_modo.config(command=self.controlador.cambiar_modo)
        self.btn_v.config(command=self.controlador.toggle_v)
        self.btn_c.config(command=self.controlador.toggle_c)

    def actualizar(self, t, h, modo, v, c, f):
        self.lbl_temp.config(text=f"{t}°C")
        self.lbl_hum.config(text=f"Humedad: {h}%")
        self.btn_modo.config(text="MANUAL" if modo else "AUTO", bg="#f39c12" if modo else "#27ae60")
        self.canvas.itemconfig(self.ind_v, fill="#2ecc71" if v else "#333333")
        self.canvas.itemconfig(self.ind_c, fill="#e74c3c" if c else "#333333")
        self.canvas.itemconfig(self.ind_f, fill="#3498db" if f else "#333333")

    def popup_error(self, msg):
        messagebox.showerror("ALERTA DE SEGURIDAD", msg)
