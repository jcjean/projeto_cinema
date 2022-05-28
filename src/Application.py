from cProfile import label
import tkinter as tk
from tkinter import *
from turtle import color
from PIL import ImageTk, Image
from Cine import Cine

root = tk.Tk()

class Application:
    def __init__(self, z = 0):
        self.cineData = Cine()
        self.selectedRoom = z
        self.selectedFilm = 0
        self.root = root
        self.imgBg = ImageTk.PhotoImage(Image.open("src/assets/imgs/background.png").resize([self.root.winfo_screenwidth(), self.root.winfo_screenheight()]))
        self.imgFilm = []
        self.tela()
        self.rooms()
        for i in range(1 , 7):
            if i <= 3:
                self.Films(i/10 * 3, 0.2, i-1, self.cineData.rooms[self.selectedRoom].films[i-1].photoEnd, self.cineData.rooms[1].films[i-1].dataIni)
            else:
                self.Films((i-3)/10 * 3, 0.6, i-1, self.cineData.rooms[self.selectedRoom].films[i-1].photoEnd, self.cineData.rooms[1].films[i-1].dataIni)
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
        #root.attributes("-fullscreen", True)
        label1 = Label(root, image = self.imgBg) 
        label1.pack(expand=True)
    
    def toggle_fullscreen(self, event=None):
        self.state = not self.state
        self.root.attributes("-fullscreen", self.state)

    def end_fullscreen(self, event=None):
        self.state = False
        self.root.attributes("-fullscreen", False)

    def rooms(self):
        self.frameRooms = Frame(self.root, background="black")
        self.frameRooms.place(relx=0.425, rely=0.05, relwidth= 0.1, relheight= 0.05)
        self.labelRooms = Label(self.frameRooms, text=f'{self.cineData.rooms[self.selectedRoom].name}', bg="black",fg="white",font="robotomono 20 bold",anchor="center")
        self.labelRooms.pack(expand=True)

        self.buttonPreviousRoom = Button(self.root, bg="white", fg="black", text="PREVIOUS", font=("robotomono", 15, "bold"), command= lambda: self.selectRoom(-1))
        self.buttonPreviousRoom.place(relx=0.365, rely=0.05, relwidth= 0.06, relheight= 0.05)
        self.buttonNextRoom = Button(self.root, bg="white", fg="black", text="NEXT", font=("robotomono", 15, "bold"), command= lambda: self.selectRoom(1))
        self.buttonNextRoom.place(relx=0.525, rely=0.05, relwidth= 0.06, relheight= 0.05)
        
    def Films(self, x, y, z, photo, data):
        self.frameFilms = Frame(self.root, bg="red")
        self.imgFilm.append(ImageTk.PhotoImage(Image.open(photo).resize([int(self.frameFilms.winfo_screenwidth()*0.15), int(self.frameFilms.winfo_screenheight()*0.3)])))
        labelFilmPhoto = Label(self.frameFilms, image = self.imgFilm[z])
        labelFilmPhoto.pack(expand=True)
        labelFilmData = Button(self.root, text=data, bg="black", foreground="white", font=("robotomono", 20, "bold"), anchor="center", bd="0", command= lambda: self.selectFilm(z))
        labelFilmData.place(relx= x-0.173, rely= y+0.30, relwidth= 0.1, relheight= 0.05)
        self.frameFilms.place(relx= x-0.2, rely= y, relwidth= 0.15, relheight= 0.3)

    def selectFilm(self, z):
        self.selectedFilm = z
        self.tela2()

    def selectRoom(self, z):
        if z == -1 and self.selectedRoom == 0:
            self.selectedRoom = 1
        elif z == 1 and self.selectedRoom == 1:
            self.selectedRoom = 0
        else:
            self.selectedRoom += z
        root.destroy
        Application(self.selectedRoom)
    
    def tela2(self):
        self.tela_dois = tk.Toplevel()
        self.imgCadeiras = ImageTk.PhotoImage(Image.open("src/assets/imgs/cadeiras_cinema.png"))
        self.tela_dois.title("Projeto Cinema")
        self.tela_dois.geometry(f'{self.root.winfo_screenwidth()}x{self.root.winfo_screenheight()}')
        self.tela_dois.minsize(width=488, height=788)
        self.tela_dois.iconbitmap('src/assets/icons/icon.ico')
        self.tela_dois.state('zoomed')
        #self.tela_dois.attributes("-fullscreen", True)
        self.lb_tela2 = Label(self.tela_dois, image=self.imgBg)
        self.lb_tela2.pack(expand=True)
        #self.tela_dois.bind("<F11>", self.toggle_fullscreen)
        #self.tela_dois.bind("<Escape>", self.end_fullscreen)
        self.infos()
        self.btCancelar()
        self.btConfirmar()
        self.seatButtons()

    def infos(self):
        label1 = Label(self.tela_dois, text=self.cineData.rooms[1].films[self.selectedFilm].nameFilm, bg="black", fg="white", font="robotomono 22 bold", anchor="center")
        label1.place(relx=0.40, rely=0.01, relwidth=0.15, relheight=0.035)

        label2 = Label(self.tela_dois, text="Nome:", bg="black",fg="white",font="robotomono 12 bold", anchor=W)
        label2.place(relx=0.40, rely=0.055, relwidth=0.05, relheight=0.022)
        nomeCliente = Entry(self.tela_dois)
        nomeCliente.place(relx=0.45, rely=0.055, relwidth=0.10, relheight=0.022)

        label3 = Label(self.tela_dois, text="Telefone:",bg="black",fg="white",font="robotomono 12 bold",anchor=W)
        label3.place(relx=0.40, rely=0.083, relwidth=0.05, relheight=0.022)
        numeroCliente = Entry(self.tela_dois)
        numeroCliente.place(relx=0.45, rely=0.083, relwidth=0.10, relheight=0.022)
    
    def btCancelar(self):
        button1 = Button(self.tela_dois, text="Cancelar", background="red",font="robotomono 11 bold", anchor="center", command=self.tela_dois.destroy)
        button1.place(relx=0.40, rely=0.12, relwidth=0.05, relheight=0.04)

    def btConfirmar(self):
        button2 = Button(self.tela_dois, text="Confirmar", background="#80ff80",font="robotomono 11 bold", anchor="center")
        button2.place(relx=0.50, rely=0.12, relwidth=0.05, relheight=0.04)

    def seatButtons(self):
        a = 0
        for i in range(1, 11):
            for j in range(1, 21):
                if j < 11:
                    button = Button(self.tela_dois, text=self.cineData.rooms[0].films[self.selectedFilm].seats[a].id, background="cyan")
                    button.place(relx= j/46+0.2, rely= i/15+0.2, relwidth=0.020 , relheight=0.04)
                else:
                    button = Button(self.tela_dois, text=self.cineData.rooms[0].films[self.selectedFilm].seats[a].id, background="cyan")
                    button.place(relx= j/46+0.3, rely= i/15+0.2, relwidth=0.02 , relheight=0.04)
                a+=1

Application()