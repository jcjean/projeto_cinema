from cProfile import label
import tkinter as tk
from tkinter import *
from turtle import color
from PIL import ImageTk, Image
from Cine import Cine

root = tk.Tk()

class Application:
    def __init__(self):
        cineData = Cine()
        self.root = root
        self.imgBg = ImageTk.PhotoImage(Image.open("src/assets/imgs/background.png").resize([self.root.winfo_screenwidth(), self.root.winfo_screenheight()]))
        self.imgFilm = []
        self.tela()
        self.rooms()
        for i in range(1 , 7):
            if i <= 3:
                self.Films(i/10 * 3, 0.2, i-1, cineData.rooms[1].films[i-1].photoEnd, cineData.rooms[1].films[i-1].dataIni)
            else:
                self.Films((i-3)/10 * 3, 0.6, i-1, cineData.rooms[1].films[i-1].photoEnd, cineData.rooms[1].films[i-1].dataIni)
        self.proximaTelaButton()
        self.root.bind("<F11>", self.toggle_fullscreen)
        self.root.bind("<Escape>", self.end_fullscreen)
        root.mainloop()

    def tela(self):
        self.root.title("Projeto Cinema")
        self.root.geometry(f'{self.root.winfo_screenwidth()}x{self.root.winfo_screenheight()}')
        self.root.resizable(True, True)
        self.root.minsize(width=588, height=888)
        self.root.iconbitmap('src/assets/icons/icon.ico')
        root.state('zoomed')
        root.attributes("-fullscreen", True)
        label1 = Label(root, image = self.imgBg) 
        label1.pack(expand=True)
    
    def toggle_fullscreen(self, event=None):
        self.state = not self.state
        self.root.attributes("-fullscreen", self.state)

    def end_fullscreen(self, event=None):
        self.state = False
        self.root.attributes("-fullscreen", False)

    def rooms(self):
        self.frameRooms = Frame(self.root,background="Black")
        self.frameRooms.place(relx=0.37, rely=0.05, width= 300, height= 100, )
        self.labelRooms = Label(self.frameRooms, text="SALA", bg="Black",fg="White",font="Times 20 bold",anchor=W)
        self.labelRooms.place(x=120,y=10)
        
    def Films(self, x, y, z, photo, data):
        self.frameFilms = Frame(self.root, bg="red")
        self.imgFilm.append(ImageTk.PhotoImage(Image.open(photo).resize([int(self.frameFilms.winfo_screenwidth()*0.15), int(self.frameFilms.winfo_screenheight()*0.3)])))
        labelFilmPhoto = Label(self.frameFilms, image = self.imgFilm[z])
        labelFilmPhoto.pack(expand=True)
        labelFilmData = Button(self.root, text=data, bg="black", foreground="white", font=("robotomono", 20, "bold"), anchor="center", bd="0", command=self.tela2)
        labelFilmData.place(relx= x-0.173, rely= y+0.30, relwidth= 0.1, relheight= 0.05)
        self.frameFilms.place(relx= x-0.2, rely= y, relwidth= 0.15, relheight= 0.3)
    
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