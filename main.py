from app.app import CalculadoraApp

if __name__ == "__main__":
    app = CalculadoraApp()
    app.geometry("{0}x{1}+0+0".format(app.winfo_screenwidth(), app.winfo_screenheight()))  # Utiliza el espacio disponible
    app.mainloop()