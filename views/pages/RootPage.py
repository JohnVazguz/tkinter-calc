import tkinter as tk
from tkinter import ttk, messagebox
class PaginaOperacionRaiz(ttk.Frame):
    def __init__(self, master, operacion, nombre_operacion):
        super().__init__(master)
        self.master = master
        self.operacion = operacion
        self.nombre_operacion = nombre_operacion

        self.create_widgets()

    def create_widgets(self):
        label_titulo = ttk.Label(self, text=f"{self.nombre_operacion}")
        label_titulo.pack(side=tk.TOP, pady=10)

        label_radicando = ttk.Label(self, text="Radicando:")
        label_radicando.pack(side=tk.LEFT, padx=5)
        entry_radicando = ttk.Entry(self)
        entry_radicando.pack(side=tk.LEFT, padx=5)

        label_indice = ttk.Label(self, text="Índice:")
        label_indice.pack(side=tk.LEFT, padx=5)
        entry_indice = ttk.Entry(self)
        entry_indice.pack(side=tk.LEFT, padx=5)

        button_calcular = ttk.Button(self, text="Calcular", command=lambda: self.realizar_operacion(entry_radicando.get(), entry_indice.get()))
        button_calcular.pack(side=tk.TOP, pady=10)

        button_volver = ttk.Button(self, text="Volver a Principal", command=self.volver_a_principal)
        button_volver.pack(side=tk.TOP, pady=10)

    def volver_a_principal(self):
        self.master.frame.pack(expand=True, fill="both")
        self.pack_forget()

    def realizar_operacion(self, radicando, indice):
        try:
            resultado = self.operacion(float(radicando), float(indice))
            messagebox.showinfo("Resultado", f"El resultado de {self.nombre_operacion} es: {resultado}")
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese números válidos.")