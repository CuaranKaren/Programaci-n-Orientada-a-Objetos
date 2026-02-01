
"""
Created on Thu Dec 18 15:02:08 2025

@author: ke802
"""

import tkinter as tk
from tkinter import messagebox
import random

REGALOS = [
    "Babuchas del Gring",
    "Peluche",
    "Estuche celular",
    "Rompecabezas",
    "Galletas",
    "Locion",
    "Joyero",
    "Calcetines",
    "Blusa",
    "Porta retrato",
    "Collar",
    "Tres leches",
    "Tripode",
    "Bloqueador",
    "Labial",
    "Guantes",
    "Botas de frio",
    "Gabardina",
    "Gafas",
    "Manilla Pandora",
    "Cartera",
    "Pantalon",
    "Gorro de Santa",
    "Cupon de 500 dolares"
]

random.shuffle(REGALOS)

ICONOS = [
    "🎄", "🎁", "⭐", "❄️", "⛄", "🔔",
    "🕯️", "🍪", "🦌", "🎅", "🌟", "🥛"
]

COLORES = [
    "#C62828", "#2E7D32", "#F9A825", "#1565C0",
    "#6A1B9A", "#EF6C00", "#00838F", "#AD1457"
]

class CalendarioApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Calendario de Adviento")
        self.master.resizable(False, False)

        self.canvas = tk.Canvas(
            self.master,
            width=720,
            height=520,
            bg="#FDF6EC"
        )
        self.canvas.pack(padx=20, pady=20)

        self.frame = tk.Frame(self.canvas, bg="#FDF6EC")
        self.canvas.create_window((360, 260), window=self.frame)

        self.crear_botones()

    def crear_botones(self):
        filas = 4
        columnas = 6
        indice_icono = 0

        for i in range(filas):
            for j in range(columnas):
                dia = (i * columnas) + j + 1

                icono = ICONOS[indice_icono % len(ICONOS)]
                color = COLORES[(dia - 1) % len(COLORES)]
                indice_icono += 1

                boton = tk.Button(
                    self.frame,
                    text=f"{icono}\n{dia}",
                    width=10,
                    height=4,
                    bg=color,
                    fg="white",
                    font=("Arial", 12, "bold")
                )

                boton.config(
                    command=lambda d=dia, b=boton: self.abrir_regalo(d, b)
                )

                boton.grid(row=i, column=j, padx=6, pady=6)

    def abrir_regalo(self, dia, boton):
        regalo = REGALOS[dia - 1]

        messagebox.showinfo(
            f"Día {dia}",
            f"Regalo del día {dia}:\n\n{regalo}"
        )

        boton.config(
            text=f"✔\n{dia}",
            state="disabled",
            bg="#9E9E9E"
        )

if __name__ == "__main__":
    root = tk.Tk()
    app = CalendarioApp(root)
    root.mainloop()
