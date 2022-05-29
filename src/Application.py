import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from Cine import Cine
import re

class Application:

    def __init__(self, selectedRoom, selectedFilm):
        self.root = tk.Tk()
        self.cineData = Cine()
        self.selectedRoom = selectedRoom
        self.selectedFilm = selectedFilm
        self.imgFilm = []
        self.selectedSeats = []
        self.imgBg = ImageTk.PhotoImage(Image.open("src/assets/imgs/background.png").resize([self.root.winfo_screenwidth(), self.root.winfo_screenheight()]))
        self.root.title("Projeto Cinema")
        self.root.geometry(f'{self.root.winfo_screenwidth()}x{self.root.winfo_screenheight()}')
        self.root.resizable(True, True)
        self.root.minsize(width=588, height=888)
        self.root.iconbitmap('src/assets/icons/icon.ico')
        self.root.state('zoomed')
        self.root.attributes("-fullscreen", True)
        self.root.bind("<F11>", self.toggleFullscreen)
        self.root.bind("<Escape>", self.endWindow)
        self.tela()
        self.root.mainloop()

    def tela(self):
        self.telaLabel = Label(self.root, image = self.imgBg) 
        self.telaLabel.pack(expand=True)
        self.imgFilm = []
        self.rooms()
        for i in range(1 , 7):
            if i <= 3:
                self.Films(i/10 * 3, 0.2, i-1, self.cineData.rooms[self.selectedRoom].films[i-1].photoEnd, self.cineData.rooms[self.selectedRoom].films[i-1].dataIni)
            else:
                self.Films((i-3)/10 * 3, 0.6, i-1, self.cineData.rooms[self.selectedRoom].films[i-1].photoEnd, self.cineData.rooms[self.selectedRoom].films[i-1].dataIni)
    
    def toggleFullscreen(self, event=None):
        self.state = not self.root.attributes("-fullscreen")
        self.root.attributes("-fullscreen", self.state)
    
    def endWindow(self, event=None):
        self.root.destroy()

    def rooms(self):
        self.frameRooms = Frame(self.telaLabel, bg="black")
        self.frameRooms.place(relx=0.425, rely=0.05, relwidth= 0.1, relheight= 0.05)
        self.labelRooms = Label(self.frameRooms, text=f'{self.cineData.rooms[self.selectedRoom].name}', bg="black",fg="white",font=("robotomono", 20, "bold"),anchor="center")
        self.labelRooms.pack(expand=True)

        self.buttonPreviousRoom = Button(self.telaLabel, bg="white", fg="black", text="ANTERIOR", font=("robotomono", 13, "bold"), command= lambda: self.selectRoom(-1))
        self.buttonPreviousRoom.place(relx=0.355, rely=0.05, relwidth= 0.07, relheight= 0.04)
        self.buttonNextRoom = Button(self.telaLabel, bg="white", fg="black", text="PRÓXIMO", font=("robotomono", 13, "bold"), command= lambda: self.selectRoom(1))
        self.buttonNextRoom.place(relx=0.525, rely=0.05, relwidth= 0.07, relheight= 0.04)

    def Films(self, x, y, z, photo, data):
        self.frameFilms = Frame(self.telaLabel, bg="red")
        self.imgFilm.append(ImageTk.PhotoImage(Image.open(photo).resize([int(self.frameFilms.winfo_screenwidth()*0.15), int(self.frameFilms.winfo_screenheight()*0.3)])))
        labelFilmPhoto = Label(self.frameFilms, image = self.imgFilm[z])
        labelFilmPhoto.pack(expand=True)
        
        labelFilmData = Button(self.telaLabel, text=self.checkSeats(data, z, 0), bg="black", fg=self.checkSeats(data, z, 1), font=("robotomono", 20, "bold"), anchor="center", bd="0", command= lambda: self.selectFilm(z))
        labelFilmData.place(relx= x-0.173, rely= y+0.30, relwidth= 0.1, relheight= 0.05)
        self.frameFilms.place(relx= x-0.2, rely= y, relwidth= 0.15, relheight= 0.3)

    def selectFilm(self, filmIndex):
        self.selectedFilm = filmIndex   
        self.telaLabel.pack_forget()
        self.tela2()

    def selectRoom(self, z):
        if z == -1 and self.selectedRoom == 0:
            self.selectedRoom = len(self.cineData.rooms)-1
        elif z == 1 and self.selectedRoom == len(self.cineData.rooms)-1:
            self.selectedRoom = 0
        else:
            self.selectedRoom += z
        self.telaLabel.pack_forget()
        self.tela()
    
    def checkSeats(self, data, film, operation):
        if operation == 0:
            for seat in self.cineData.rooms[self.selectedRoom].films[film].seats:
                if seat.occupied == False:
                    return data
            return "CHEIO"
        else:
            for seat in self.cineData.rooms[self.selectedRoom].films[film].seats:
                if seat.occupied == False:
                    return "white"
            return "red"

    def tela2(self):
        self.tela2Label = Label(self.root, image = self.imgBg) 
        self.tela2Label.pack(expand=True)
        self.selectedSeats = []
        self.infos()
        self.btCancelar()
        self.btConfirmar()        
        self.lbAlert()
        self.seatButtons()

    def infos(self):
        label1 = Label(self.tela2Label, text=self.cineData.rooms[self.selectedRoom].films[self.selectedFilm].nameFilm, bg="black", fg="white", font="robotomono 22 bold", anchor="center")
        label1.place(relx=0.41, rely=0.01, relwidth=0.17, relheight=0.035)

        label2 = Label(self.tela2Label, text="Nome:", bg="black",fg="white",font=("robotomono", 12, "bold"), anchor=W)
        label2.place(relx=0.41, rely=0.055, relwidth=0.05, relheight=0.022)
        self.nomeCliente = Entry(self.tela2Label)
        self.nomeCliente.place(relx=0.47, rely=0.058, relwidth=0.10, relheight=0.022)

        label3 = Label(self.tela2Label, text="Telefone:",bg="black",fg="white",font=("robotomono", 12, "bold"),anchor=W)
        label3.place(relx=0.41, rely=0.083, relwidth=0.06, relheight=0.022)
        self.numeroCliente = Entry(self.tela2Label)
        self.numeroCliente.place(relx=0.47, rely=0.085, relwidth=0.10, relheight=0.022)

    def btCancelar(self):
        button1 = Button(self.tela2Label, text="Cancelar", bg="red",font=("robotomono", 11, "bold"), anchor="center", command=self.cancelOperation)
        button1.place(relx=0.41, rely=0.12, relwidth=0.06, relheight=0.04)

    def btConfirmar(self):
        button2 = Button(self.tela2Label, text="Confirmar", bg="#80ff80",font=("robotomono", 11, "bold"), anchor="center" , command= lambda : self.confirmSeats(self.nomeCliente.get(), self.numeroCliente.get(), self.selectedSeats))
        button2.place(relx=0.51, rely=0.12, relwidth=0.06, relheight=0.04)
    
    def lbAlert(self):
        self.alertLabel = Label(self.tela2Label, bg="black", fg="#ff0000", font=("robotomono", 12, "bold"), anchor="center")
        self.alertLabel.place(relx=0.31, rely=0.17, relwidth=0.35, relheight=0.04)

    def cancelOperation(self):
        self.tela2Label.pack_forget()
        self.tela()

    def confirmSeats(self, name, number, seats):
        patternName = "^[A-Za-z]*$"
        patternNumber = "^[0-9]*$"
        nameBool = bool(re.match(patternName, name))
        numberBool = bool(re.match(patternNumber, str(number)))
        if nameBool == False:
            self.alertLabel["text"] = "Apenas letras no Nome!"
        elif name == "":
            self.alertLabel["text"] = "Digite o Nome!"
        elif numberBool == False:
            self.alertLabel["text"] = "Apenas Números no Telefone!"
        elif number == "":
            self.alertLabel["text"] = "Digite o Número!"
        elif len(seats) == 0:
            self.alertLabel["text"] = "Necessário pelo menos um assento marcado!"
        else:
            self.cineData.rooms[self.selectedRoom].films[self.selectedFilm].registerSeats(name, number, seats)
            self.tela2Label.pack_forget()
            self.tela()
        


    def selectSeat(self, id, button):
        if  button["bg"] == "blue":
            self.selectedSeats.append(id)
            button["bg"] = "darkorange"
        elif  button["bg"] == "darkorange":
            for seat in self.selectedSeats:
                if seat == id:
                    self.selectedSeats.remove(seat)
            button["bg"] = "blue"

    def seatButtons(self):
        a = 0
        for i in range(1, 11):
            for j in range(1, 21):
                if j < 11:
                    button = Button(self.tela2Label, text=self.cineData.rooms[self.selectedRoom].films[self.selectedFilm].seats[a].id, bg="blue", fg="white", font=("robotomono", 10, "bold"), relief=FLAT, command=self.selectSeat)
                    if self.cineData.rooms[self.selectedRoom].films[self.selectedFilm].seats[a].occupied == True:
                        button["bg"] = "red"
                        button["state"] = "disabled"
                    button["command"] = lambda button=button: self.selectSeat(button["text"],button)
                    button.place(relx= j/46+0.2, rely= i/15+0.2, relwidth=0.020 , relheight=0.04)
                else:
                    button = Button(self.tela2Label, text=self.cineData.rooms[self.selectedRoom].films[self.selectedFilm].seats[a].id, bg="blue", fg="white", font=("robotomono", 10, "bold"), relief=FLAT, command=self.selectSeat)
                    if self.cineData.rooms[self.selectedRoom].films[self.selectedFilm].seats[a].occupied == True:
                        button["bg"] = "red"
                        button["state"] = "disabled"
                    button["command"] = lambda button=button: self.selectSeat(button["text"],button)
                    button.place(relx= j/46+0.3, rely= i/15+0.2, relwidth=0.02 , relheight=0.04)
                a+=1

Application(0, 0)