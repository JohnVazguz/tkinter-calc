import tkinter as tk

from tkinter import ttk, messagebox
from tkinter import scrolledtext
from maths.addition import addition
from maths.substraction import substraction
from maths.multiplication import multiplication
from maths.division import division
from maths.power import power
from maths.root import root
from maths.logarithm import logarithm
from maths.QuadraticEquation import calc_quadratic_formula

from views.pages.PowerPage import PaginaOperacionPotencia
from views.pages.RootPage import PaginaOperacionRaiz
from views.pages.LogPage import PaginaOperacionLogaritmo
from views.pages.QuadraticEquationPage import PaginaOperacionEcuacionCuadratica
from views.pages.BasicPage import PaginaOperacion

from views.util.ScrolledFrame import ScrolledFrame

class CalculadoraApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculadora")
        self.geometry("600x400")  # Ajusta el tamaño de la ventana principal

        self.style = ttk.Style()
        self.style.theme_use("clam")

        self.create_widgets()

    def create_widgets(self):
        self.frame = ttk.Frame(self, padding="10")
        self.frame.pack(expand=True, fill="both")  # Cambia a pack para evitar superposiciones

        button_suma = ttk.Button(self.frame, text="Suma", command=lambda: self.mostrar_pagina_operacion(addition, "Suma"))
        button_resta = ttk.Button(self.frame, text="Resta", command=lambda: self.mostrar_pagina_operacion(substraction, "Resta"))
        button_multiplicacion = ttk.Button(self.frame, text="Multiplicación", command=lambda: self.mostrar_pagina_operacion(multiplication, "Multiplicación"))
        button_division = ttk.Button(self.frame, text="División", command=lambda: self.mostrar_pagina_operacion(division, "División"))
        button_potencia = ttk.Button(self.frame, text="Potencia", command=lambda: self.mostrar_pagina_potencia())
        button_raiz = ttk.Button(self.frame, text="Raíz", command=lambda: self.mostrar_pagina_raiz())
        button_logaritmo = ttk.Button(self.frame, text="Logaritmo", command=lambda: self.mostrar_pagina_logaritmo())
        button_ecuacion_cuadratica = ttk.Button(self.frame, text="Ecuación Cuadrática", command=lambda: self.mostrar_pagina_ecuacion_cuadratica())

        button_suma.pack(side=tk.LEFT, padx=5, pady=10, expand=True, fill="both")
        button_resta.pack(side=tk.LEFT, padx=5, pady=10, expand=True, fill="both")
        button_multiplicacion.pack(side=tk.LEFT, padx=5, pady=10, expand=True, fill="both")
        button_division.pack(side=tk.LEFT, padx=5, pady=10, expand=True, fill="both")
        button_potencia.pack(side=tk.LEFT, padx=5, pady=10, expand=True, fill="both")
        button_raiz.pack(side=tk.LEFT, padx=5, pady=10, expand=True, fill="both")
        button_logaritmo.pack(side=tk.LEFT, padx=5, pady=10, expand=True, fill="both")
        button_ecuacion_cuadratica.pack(side=tk.LEFT, padx=5, pady=10, expand=True, fill="both")

    def mostrar_pagina_potencia(self):
        pagina = PaginaOperacionPotencia(self, power, "Potencia")
        pagina.pack(expand=True, fill="both")
        self.frame.pack_forget()

    def mostrar_pagina_raiz(self):
        pagina = PaginaOperacionRaiz(self, root, "Raíz")
        pagina.pack(expand=True, fill="both")
        self.frame.pack_forget()

    def mostrar_pagina_logaritmo(self):
        pagina = PaginaOperacionLogaritmo(self, logarithm, "Logaritmo")
        pagina.pack(expand=True, fill="both")
        self.frame.pack_forget()

    def mostrar_pagina_ecuacion_cuadratica(self):
        pagina = PaginaOperacionEcuacionCuadratica(self, calc_quadratic_formula)
        pagina.pack(expand=True, fill="both")
        self.frame.pack_forget()

    def mostrar_pagina_operacion(self, operacion, nombre_operacion):
        pagina = PaginaOperacion(self, operacion, nombre_operacion)
        pagina.pack(expand=True, fill="both")
        self.frame.pack_forget()