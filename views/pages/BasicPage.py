import tkinter as tk
from tkinter import ttk, messagebox

from views.util.ScrolledFrame import ScrolledFrame

def crear_scrolled_frame(parent):
    return ScrolledFrame(parent)

class PaginaOperacion(ttk.Frame):
    MAX_NUMEROS = 20  # Aumentado el límite máximo

    def __init__(self, master, operacion, nombre_operacion):
        super().__init__(master)
        self.master = master
        self.operacion = operacion
        self.nombre_operacion = nombre_operacion

        self.labels = []
        self.entries = []

        self.create_widgets()

    def create_widgets(self):
        label_titulo = ttk.Label(self, text=f"{self.nombre_operacion}")
        label_titulo.grid(row=0, column=0, pady=10, columnspan=4, sticky="nsew")

        scrolled_frame = crear_scrolled_frame(self)
        scrolled_frame.grid(row=1, column=0, pady=10, columnspan=4, sticky="nsew")

        self.create_label_entry(scrolled_frame.scrollable_frame)
        self.create_label_entry(scrolled_frame.scrollable_frame)  # Agregar otro espacio por defecto

        button_agregar_entrada = ttk.Button(self, text="Añadir Número", command=lambda: self.create_label_entry(scrolled_frame.scrollable_frame))
        button_calcular = ttk.Button(self, text="Calcular", command=self.realizar_operacion)
        button_volver = ttk.Button(self, text="Volver", command=self.volver_a_principal)

        button_agregar_entrada.grid(row=2, column=0, pady=10, padx=5, columnspan=4, sticky="nsew")
        button_calcular.grid(row=3, column=0, pady=10, padx=5, columnspan=4, sticky="nsew")
        button_volver.grid(row=4, column=0, pady=10, padx=5, columnspan=4, sticky="nsew")

        # Configuración de pesos de fila y columna para expandir
        for i in range(1, 5):
            self.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.grid_columnconfigure(i, weight=1)

    def create_label_entry(self, container):
        if len(self.labels) >= self.MAX_NUMEROS:
            messagebox.showinfo("Límite Alcanzado", f"No se pueden agregar más de {self.MAX_NUMEROS} números.")
            return

        row_index = len(self.labels) // 4
        col_index = len(self.labels) % 4

        label = ttk.Label(container, text=f"Número {len(self.labels) + 1}:")
        entry = ttk.Entry(container)
        label.grid(row=row_index, column=col_index * 2, pady=5, padx=5, sticky="nsew")
        entry.grid(row=row_index, column=col_index * 2 + 1, pady=5, padx=5, sticky="nsew")
        self.labels.append(label)
        self.entries.append(entry)

    def realizar_operacion(self):
        try:
            numeros = [float(entry.get()) for entry in self.entries]
            resultado = self.operacion(*numeros)
            self.mostrar_resultado(resultado)
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese números válidos.")

    def mostrar_resultado(self, resultado):
        messagebox.showinfo("Resultado", f"El resultado de {self.nombre_operacion} es: {resultado}")

    def volver_a_principal(self):
        self.master.frame.pack(expand=True, fill="both")
        self.pack_forget()
