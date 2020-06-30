import requests
from tkinter import *
import tkinter as tk
from tkinter import ttk,font,messagebox
class App():
    __ventana=None
    __valorD=None
    __valorP=None
    def __init__(self):
        self.__ventana=Tk()
        self.__ventana.resizable(0,0)
        self.__ventana.title("Conversor de moneda")
        self.contenedor=ttk.Frame(self.__ventana,borderwidth=3,padding=(30,20),relief="raised")
       
        self.__valorD=StringVar()
        self.__valorP=StringVar()
        self.entrada=ttk.Entry(self.contenedor,textvariable=self.__valorD,width=7)
        ttk.Label(self.contenedor,text="Dólares").grid(row=1,column=2)
        ttk.Label(self.contenedor,text="Es equivalente a:").grid(row=2,column=0,sticky=(W,E))
        self.__valorD.trace("w",self.calcular)
        ttk.Label(self.contenedor,textvariable=self.__valorP,width=8).grid(row=2,column=1,sticky=E)
        ttk.Label(self.contenedor,text="Pesos").grid(row=2,column=2)
        ttk.Button(self.contenedor,text="Salir",command=self.__ventana.destroy).grid(row=3,column=2)
        self.entrada.focus_set()
        self.contenedor.grid(column=0,row=0)
        self.entrada.grid(row=1,column=1)
        for child in self.contenedor.winfo_children():
            child.grid_configure(padx=5, pady=5)
        self.__ventana.mainloop()
    def calcular(self,*args):
        valor=self.entrada.get()
        if(valor!=""):
            try:
                respuesta=requests.get("https://www.dolarsi.com/api/api.php?type=dolar")
                dic=respuesta.json()
                dolares=dic[0]["casa"]["venta"]
                dolares=float(dolares.replace(",","."))
                self.__valorP.set(dolares*float(valor))
            except ValueError:
                messagebox.showerror(title="Error de tipo",message="Solo se adminten numeros y .")
                self.__valorD.set("")
                self.entrada.focus_set()
            except:
                messagebox.showerror(title="Error en la conexion",message="No se pudo conectar a la api")
        else:
            self.__valorP.set("")