import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from Cine import Cine

root = tk.Tk()

class HeritageWindow:
    def __init__(self, cineData):
        if cineData == None:
            self.cineData = Cine()
        else:
            self.cineData = cineData
        self.root = root
        self.imgBg = ImageTk.PhotoImage(Image.open("src/assets/imgs/background.png").resize([self.root.winfo_screenwidth(), self.root.winfo_screenheight()]))
        self.tela()
        self.root.bind("<F11>", self.toggleFullscreen)
        self.root.bind("<Escape>", self.endWindow)
        
    def tela(self):
        self.root.title("Projeto Cinema")
        self.root.geometry(f'{self.root.winfo_screenwidth()}x{self.root.winfo_screenheight()}')
        self.root.resizable(True, True)
        self.root.minsize(width=588, height=888)
        self.root.iconbitmap('src/assets/icons/icon.ico')
        self.root.state('zoomed')
        self.root.attributes("-fullscreen", True)
        label1 = Label(self.root, image = self.imgBg) 
        label1.pack(expand=True)

    def toggleFullscreen(self, event=None):
        self.state = not self.root.attributes("-fullscreen")
        self.root.attributes("-fullscreen", self.state)
    
    def endWindow(self, event=None):
        for widget in self.root.winfo_children():
            widget.destroy()
        self.root.destroy()