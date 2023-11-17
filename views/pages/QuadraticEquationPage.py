import tkinter as tk
from tkinter import ttk, messagebox
class PaginaOperacionEcuacionCuadratica(ttk.Frame):
    def __init__(self, master, operacion):
        super().__init__(master)
        self.master = master
        self.operacion = operacion

        self.create_widgets()

    def create_widgets(self):
        label_titulo = ttk.Label(self, text="Ecuación Cuadrática")
        label_titulo.pack(side=tk.TOP, pady=10)

        label_a = ttk.Label(self, text="Coeficiente a:")
        label_a.pack(side=tk.LEFT, padx=5)
        entry_a = ttk.Entry(self)
        entry_a.pack(side=tk.LEFT, padx=5)

        label_b = ttk.Label(self, text="Coeficiente b:")
        label_b.pack(side=tk.LEFT, padx=5)
        entry_b = ttk.Entry(self)
        entry_b.pack(side=tk.LEFT, padx=5)

        label_c = ttk.Label(self, text="Coeficiente c:")
        label_c.pack(side=tk.LEFT, padx=5)
        entry_c = ttk.Entry(self)
        entry_c.pack(side=tk.LEFT, padx=5)

        button_calcular = ttk.Button(self, text="Calcular", command=lambda: self.realizar_operacion(entry_a.get(), entry_b.get(), entry_c.get()))
        button_calcular.pack(side=tk.TOP, pady=10)
        
        button_volver = ttk.Button(self, text="Volver a Principal", command=self.volver_a_principal)
        button_volver.pack(side=tk.TOP, pady=10)

    def realizar_operacion(self, a, b, c):
        try:
            resultado = self.operacion(float(a), float(b), float(c))
            if isinstance(resultado[0], complex):
                messagebox.showinfo("Resultado", f"Las soluciones de la ecuación cuadrática son: {resultado[0]} y {resultado[1]}")
            else:
                if len(resultado) == 2:
                    messagebox.showinfo("Resultado", f"Las soluciones son: {resultado[0]} y {resultado[1]}")
                elif len(resultado) == 1:
                    messagebox.showinfo("Resultado", f"Las solucion es: {resultado[0]} ")
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese coeficientes válidos.")

    def volver_a_principal(self):
        self.master.frame.pack(expand=True, fill="both")
        self.pack_forget()