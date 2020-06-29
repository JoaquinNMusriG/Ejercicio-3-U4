from tkinter import ttk,Tk,StringVar
from tkinter.constants import *
import requests
from datetime import datetime
from functools import partial

class Aplicacion():
    __ventana=None
    __hora=None
    def __init__(self):
        self.__ventana = Tk()
        self.__ventana.title('Ejercicio 3')
        mainframe = ttk.Frame(self.__ventana, padding="5 5 12 12", relief='sunken')
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

        ttk.Label(mainframe, text="hora: ").grid(column=1, row=0, sticky=E)
        self.__hora = StringVar()
        self.__hora.set(datetime.now().time())
        ttk.Label(mainframe, textvariable=self.__hora).grid(column=2, row=0, sticky=E)

        self.boton1=ttk.Button(mainframe, text='Actualizar', command=partial(self.ej3,mainframe))
        self.boton1.grid(column=0, row=0, sticky=W)

        for child in mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)
        self.__ventana.mainloop()


    def ej3(self,mainframe):
        self.__hora.set(datetime.now().time())
        r = requests.get('https://www.dolarsi.com/api/api.php?type=valoresprincipales')
        x = r.json()
        i=2
        band = False
        for elemento in x:
            if ('casa' in elemento):
                if ('compra' in elemento['casa']) & ('venta' in elemento['casa']) & ('nombre' in elemento['casa']):
                    if ('Dolar' in elemento['casa']['nombre']):
                        if not band:
                            ttk.Label(mainframe, text="Compra").grid(column=1, row=1, sticky=E)
                            ttk.Label(mainframe, text="Venta").grid(column=2, row=1, sticky=E)
                            band = True
                        ttk.Label(mainframe, text=str(elemento['casa']['nombre'])).grid(column=0, row=i, sticky=W)
                        compra = ttk.Entry(mainframe, width=10)
                        venta = ttk.Entry(mainframe, width=10)
                        compra.grid(padx=5, pady=5, row=i, column=1)
                        venta.grid(padx=5, pady=5, row=i, column=2)
                        compra.insert(0, str(elemento['casa']['compra']))
                        venta.insert(0, str(elemento['casa']['venta']))
                        i += 1
