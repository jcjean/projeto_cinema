import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image

root = tk.Tk()

class Application:
    def __init__(self):
        self.root = root
        self.imgBg = ImageTk.PhotoImage(Image.open("src/assets/imgs/background.png"))
        self.tela()
        self.rooms()
        self.addRoom()
        self.proximaTelaButton()
        root.mainloop()

    def tela(self):
        self.root.title("Projeto Cinema")
        self.root.geometry("1366x760")
        self.root.resizable(True, True)
        self.root.minsize(width=488, height=788)
        self.root.iconbitmap('src/assets/icons/icon.ico')
        label1 = Label(root, image = self.imgBg) 
        label1.place(x=0, y=0, relwidth=1, relheight=1)

    def rooms(self):
        self.frameRooms = Frame(self.root,background="Black")
        self.frameRooms.place(x= 500, y= 20, width= 300, height= 100, )
        self.labelRooms = Label(self.frameRooms, text="SALA", bg="Black",fg="White",font="Times 20 bold",anchor=W)
        self.labelRooms.place(x=120,y=10)
        
    def addRoom(self):
        self.frameAddRoom = Frame(self.root)
        self.frameAddRoom.place(relx= 0.1, rely= 0.6, relwidth= 0.8, relheight= 0.2)
    
    def tela2(self):
        self.tela_dois = tk.Toplevel()
        self.imgCadeiras = ImageTk.PhotoImage(Image.open("src/assets/imgs/cadeiras_cinema.png"))
        self.tela_dois.title("Projeto Cinema")
        self.tela_dois.geometry("1366x760")
        self.tela_dois.minsize(width=488, height=788)
        self.lb_tela2 = tk.Label(self.tela_dois, background="#003366")
        self.lb_tela2.place(x=0,y=0,relwidth=1,relheight=1)
        self.infos()
        self.btCancelar()
        self.btConfirmar()
        self.esboço()

    def proximaTelaButton(self):
        self.btTrocaTela = tk.Button(self.frameRooms, text="prox", command=self.tela2)
        self.btTrocaTela.place (x= 210, y = 14, width= 50, height=25)

    def infos(self):
        label1 = Label(self.tela_dois, text="Nome:", bg="#003366",fg="white",font="Times 12", anchor=W)
        label1.place(x=500,y=30,width=100,height=20)
        nomeCliente = Entry(self.tela_dois)
        nomeCliente.place(x=580, y=30, width=190, height=20)

        label2 = Label(self.tela_dois, text="Telefone:",bg="#003366",fg="white",font="Times",anchor=W)
        label2.place(x=500, y=70, width=100, height=20)
        numeroCliente = Entry(self.tela_dois)
        numeroCliente.place(x=580, y=70, width=190, height=20)
    
    def btCancelar(self):
        button1 = Button(self.tela_dois, text="Cancelar", background="red",font="Times 11 bold", anchor=N, command=self.tela_dois.destroy)
        button1.place(x=585,y=100,width=80, height=30)

    def btConfirmar(self):
        button2 = Button(self.tela_dois, text="Confirmar", background="#80ff80",font="Times 11 bold", anchor=N)
        button2.place(x=685,y=100,width=80, height=30)

    def esboço(self):
        labelImage = Label(self.tela_dois, image= self.imgCadeiras)
        labelImage.place(x=250,y=200, width=857, height=382)

Application()