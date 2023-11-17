import tkinter as tk
from tkinter import ttk, messagebox
class PaginaOperacionPotencia(ttk.Frame):
    def __init__(self, master, operacion, nombre_operacion):
        super().__init__(master)
        self.master = master
        self.operacion = operacion
        self.nombre_operacion = nombre_operacion

        self.create_widgets()

    def create_widgets(self):
        label_titulo = ttk.Label(self, text=f"{self.nombre_operacion}")
        label_titulo.pack(side=tk.TOP, pady=10)

        label_numero = ttk.Label(self, text="Número:")
        label_numero.pack(side=tk.LEFT, padx=5)
        entry_numero = ttk.Entry(self)
        entry_numero.pack(side=tk.LEFT, padx=5)

        label_exponente = ttk.Label(self, text="Exponente:")
        label_exponente.pack(side=tk.LEFT, padx=5)
        entry_exponente = ttk.Entry(self)
        entry_exponente.pack(side=tk.LEFT, padx=5)

        button_calcular = ttk.Button(self, text="Calcular", command=lambda: self.realizar_operacion(entry_numero.get(), entry_exponente.get()))
        button_calcular.pack(side=tk.TOP, pady=10)

        button_volver = ttk.Button(self, text="Volver a Principal", command=self.volver_a_principal)
        button_volver.pack(side=tk.TOP, pady=10)

    def realizar_operacion(self, numero, exponente):
        try:
            resultado = self.operacion(float(numero), float(exponente))
            messagebox.showinfo("Resultado", f"El resultado de {self.nombre_operacion} es: {resultado}")
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese números válidos.")

    def volver_a_principal(self):
        self.master.frame.pack(expand=True, fill="both")
        self.pack_forget()