import tkinter as tk

class SumaApp:
    def __init__(self, master):
        self.master = master
        
        master.title("Suma de valores")

        # Valores por defecto
        self.valor1 = tk.DoubleVar(value=1)
        self.valor2 = tk.DoubleVar(value=1)
        self.resultado = tk.DoubleVar(value=2)

        # Crear entrada de valores
        self.valor1_label = tk.Label(master, text="Valor 1:")
        self.valor1_entry = tk.Entry(master, textvariable=self.valor1)
        self.valor2_label = tk.Label(master, text="Valor 2:")
        self.valor2_entry = tk.Entry(master, textvariable=self.valor2)

        # Crear bullet para seleccionar la categoría
        self.categoria_label = tk.Label(master, text="Categoría:")
        self.categoria = tk.StringVar(value="AC")
        self.ac_radio = tk.Radiobutton(master, text="AC", variable=self.categoria, value="AC", command=self.actualizar_resultado)
        self.dc_radio = tk.Radiobutton(master, text="DC", variable=self.categoria, value="DC", command=self.actualizar_resultado)
        self.impulso_radio = tk.Radiobutton(master, text="Impulso", variable=self.categoria, value="Impulso", command=self.actualizar_resultado)

        # Crear salida de resultado
        self.resultado_label = tk.Label(master, text="Resultado:")
        self.resultado_entry = tk.Entry(master, textvariable=self.resultado, state="readonly")

        # Ubicar los elementos en la ventana
        self.valor1_label.grid(row=0, column=0)
        self.valor1_entry.grid(row=0, column=1)
        self.valor2_label.grid(row=1, column=0)
        self.valor2_entry.grid(row=1, column=1)

        self.categoria_label.grid(row=2, column=0)
        self.ac_radio.grid(row=2, column=1)
        self.dc_radio.grid(row=2, column=2)
        self.impulso_radio.grid(row=2, column=3)

        self.resultado_label.grid(row=3, column=0)
        self.resultado_entry.grid(row=3, column=1)

        # Actualizar resultado al modificar las entradas
        self.valor1_entry.bind("<KeyRelease>", self.actualizar_resultado)
        self.valor2_entry.bind("<KeyRelease>", self.actualizar_resultado)

    def actualizar_resultado(self, event=None):
        valor1 = self.valor1.get()
        valor2 = self.valor2.get()
        categoria = self.categoria.get()

        resultado = valor1 + valor2

        if categoria == "AC":
            resultado *= 1
        elif categoria == "DC":
            resultado *= 1
        else:
            resultado *= 1

        self.resultado.set(0)


        self.resultado.set(resultado)

root = tk.Tk()
app = SumaApp(root)
root.mainloop()

