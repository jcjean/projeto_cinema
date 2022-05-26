from tkinter import *
from PIL import ImageTk, Image
import os

janela = Tk()

class TelaDois:
    def __init__(self):
        self.janela = janela
        self.imgCadeiras = ImageTk.PhotoImage(Image.open("src/assets/imgs/cadeiras_cinema.png"))
        self.tela2()
        self.infos()
        self.btCancelar()
        self.btConfirmar()
        self.esboço()
        janela.mainloop()

    def tela2(self):
        self.janela.title("Projeto Cinema")
        lb_tela2 = Label(janela, background="#003366")
        self.janela.minsize(width=900, height=600)
        lb_tela2.place(x=0,y=0,relwidth=1,relheight=1)

    def infos(self):
        label1 = Label(janela, text="Nome:", bg="#003366",fg="white",font="Times 12", anchor=W)
        label1.place(x=500,y=30,width=100,height=20)
        nomeCliente = Entry(janela)
        nomeCliente.place(x=580, y=30, width=190, height=20)
       
        label2 = Label(janela, text="Telefone:",bg="#003366",fg="white",font="Times",anchor=W)
        label2.place(x=500, y=70, width=100, height=20)
        numeroCliente = Entry(janela)
        numeroCliente.place(x=580, y=70, width=190, height=20)
    
    def btCancelar(self):
        button1 = Button(janela, text="Cancelar", background="red",font="Times 11 bold", anchor=N)
        button1.place(x=585,y=100,width=80, height=30)

    def btConfirmar(self):
        button2 = Button(janela, text="Confirmar", background="#80ff80",font="Times 11 bold", anchor=N)
        button2.place(x=685,y=100,width=80, height=30)

    def esboço(self):
        labelImage = Label(janela, image= self.imgCadeiras)
        labelImage.place(x=250,y=200, width=857, height=382) #se aumentar o tamanho e a largura, fica um fundão branco preenchendo

TelaDois()