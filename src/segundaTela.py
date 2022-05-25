from tkinter import *
from PIL import ImageTk, Image
import os


root = Tk()

class TelaDois:
    def __init__(self):
        self.root = root
        self.imgCadeiras = ImageTk.PhotoImage(Image.open("src/assets/imgs/cadeiras_cinema.png"))
        self.tela2()
        self.infos()
        self.btCancelar()
        self.btConfirmar()
        self.esboço()
        root.mainloop()

    def tela2(self):
        lb_tela2 = Label(root, background="#003366")
        self.root.minsize(width=900, height=600)
        lb_tela2.place(x=0,y=0,relwidth=1,relheight=1)

    def infos(self):
        label1 = Label(root, text="Nome:", bg="#003366",fg="white",font="Times 12", anchor=W)
        label1.place(x=300,y=30,width=100,height=20)
        nomeCliente = Entry(root)
        nomeCliente.place(x=380, y=30, width=190, height=20)
       
        label2 = Label(root, text="Telefone:",bg="#003366",fg="white",font="Times",anchor=W)
        label2.place(x=300, y=70, width=100, height=20)
        numeroCliente = Entry(root)
        numeroCliente.place(x=380, y=70, width=190, height=20)
    
    def btCancelar(self):
        button1 = Button(root, text="Cancelar", background="red",font="Times 11 bold", anchor=N)
        button1.place(x=385,y=100,width=80, height=30)

    def btConfirmar(self):
        button2 = Button(root, text="Confirmar", background="#80ff80",font="Times 11 bold", anchor=N)
        button2.place(x=485,y=100,width=80, height=30)

    def esboço(self):
        labelImage = Label(root, image= self.imgCadeiras)
        labelImage.place(x=20,y=140, width=857, height=382) #se aumentar o tamanho e a largura, fica um fundão branco preenchendo

TelaDois()