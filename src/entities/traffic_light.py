from tkinter import *
import time

class traffic_light:
    def __init__(self, status, name, data_source) -> None:
        self.status = status
        self.name = name
        self.data_source = data_source
    def change_color(self, status):
        self.status = status
        

#pantalla principal 
traffic_lights = Tk()
traffic_lights.title("Semaforo")
traffic_lights.geometry("300x400+600+150")
traffic_lights.resizable(False,False)
traffic_lights.iconbitmap("./data-source/traffic.ico")
traffic_lights.config(bg="#808080")

#Definir tamaño
myCanvas = Canvas(traffic_lights, height=400, width= 300, bg="White")
myCanvas.pack()
myCanvas.create_rectangle(100, 50, 200, 350, fill="#808080", width=2)
myCanvas.create_oval(100, 50, 200, 150, fill="Black", width=2)
myCanvas.create_oval(100, 150, 200, 250, fill="Black", width=2)
myCanvas.create_oval(100, 250, 200, 350, fill="Black", width=2)

#Definir funciones
a = 2
def red():
    for i in range(a):
        red = myCanvas.create_oval(100, 50, 200, 150, fill="Red", width=2)
        traffic_lights.update()
        time.sleep(2.50)
def redb():
    for i in range(a):
        red = myCanvas.create_oval(100, 50, 200, 150, fill="Black", width=2)
        traffic_lights.update()
        time.sleep(0.00001)
def orange():
    for i in range(a):
        orange = myCanvas.create_oval(100, 150, 200, 250, fill="Orange", width=2)
        traffic_lights.update()
        time.sleep(1.50)
def orangeb():
    for i in range(a):
        orange = myCanvas.create_oval(100, 150, 200, 250, fill="Black", width=2)
        traffic_lights.update()
        time.sleep(0.00001)
def green():
    for i in range(a):
        green = myCanvas.create_oval(100, 250, 200, 350, fill="Green", width=2)
        traffic_lights.update()
        time.sleep(3.50)
def greenb():
    for i in range(a):
        green = myCanvas.create_oval(100, 250, 200, 350, fill="Black", width=2)
        traffic_lights.update()
        time.sleep(0.00001)

def rojo():
    red()       
    orangeb()
    greenb()

def verde():
    redb()
    greenb()
    orangeb()
    orange()
    orangeb()
    green()
    greenb()

#Looping Main Window
#traffic_lights.mainloop()
