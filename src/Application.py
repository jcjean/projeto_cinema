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
        self.filmsImages = []
        self.selectedSeats = []
        self.imageBackGround = ImageTk.PhotoImage(Image.open("src/assets/imgs/background.png").resize([self.root.winfo_screenwidth(), self.root.winfo_screenheight()]))
        self.root.title("Projeto Cinema")
        self.root.geometry(f'{self.root.winfo_screenwidth()}x{self.root.winfo_screenheight()}')
        self.root.resizable(True, True)
        self.root.minsize(width=588, height=888)
        self.root.iconbitmap('src/assets/icons/icon.ico')
        self.root.state('zoomed')
        self.root.attributes("-fullscreen", True)
        self.root.bind("<F11>", self.toggleFullscreen)
        self.root.bind("<Escape>", self.endApplication)
        self.firstWindow()
        self.root.mainloop()

    def firstWindow(self):
        self.firstWindowLabel = Label(self.root, image = self.imageBackGround) 
        self.firstWindowLabel.pack(expand=True)
        self.filmsImages = []
        self.roomsSelect()
        for i in range(1 , 7):
            if i <= 3:
                self.filmsSelect(i/10 * 3, 0.2, i-1, self.cineData.rooms[self.selectedRoom].films[i-1].photoEnd, self.cineData.rooms[self.selectedRoom].films[i-1].dataIni)
            else:
                self.filmsSelect((i-3)/10 * 3, 0.6, i-1, self.cineData.rooms[self.selectedRoom].films[i-1].photoEnd, self.cineData.rooms[self.selectedRoom].films[i-1].dataIni)
    
    def toggleFullscreen(self, event=None):
        self.state = not self.root.attributes("-fullscreen")
        self.root.attributes("-fullscreen", self.state)
    
    def endApplication(self, event=None):
        self.root.destroy()

    def roomsSelect(self):
        self.roomsFrame = Frame(self.firstWindowLabel, bg="black")
        self.roomsFrame.place(relx=0.425, rely=0.05, relwidth= 0.1, relheight= 0.05)
        self.roomsLabel = Label(self.roomsFrame, text=f'{self.cineData.rooms[self.selectedRoom].name}', bg="black",fg="white",font=("robotomono", 20, "bold"),anchor="center")
        self.roomsLabel.pack(expand=True)

        self.roomButtonPrevious = Button(self.firstWindowLabel, bg="white", fg="black", text="ANTERIOR", font=("robotomono", 13, "bold"), command= lambda: self.roomSelectIndex(-1))
        self.roomButtonPrevious.place(relx=0.355, rely=0.05, relwidth= 0.07, relheight= 0.04)
        self.roomButtonNext = Button(self.firstWindowLabel, bg="white", fg="black", text="PRÓXIMO", font=("robotomono", 13, "bold"), command= lambda: self.roomSelectIndex(1))
        self.roomButtonNext.place(relx=0.525, rely=0.05, relwidth= 0.07, relheight= 0.04)

    def filmsSelect(self, x, y, index, photo, data):
        self.filmsFrame = Frame(self.firstWindowLabel, bg="red")
        self.filmsImages.append(ImageTk.PhotoImage(Image.open(photo).resize([int(self.filmsFrame.winfo_screenwidth()*0.15), int(self.filmsFrame.winfo_screenheight()*0.3)])))
        filmLabelPhoto = Label(self.filmsFrame, image = self.filmsImages[index])
        filmLabelPhoto.pack(expand=True)
        
        filmLabelData = Button(self.firstWindowLabel, text=self.checkSeats(data, index, 0), bg="black", fg=self.checkSeats(data, index, 1), font=("robotomono", 20, "bold"), anchor="center", bd="0", command= lambda: self.filmSelectIndex(index))
        filmLabelData.place(relx= x-0.173, rely= y+0.30, relwidth= 0.1, relheight= 0.05)
        self.filmsFrame.place(relx= x-0.2, rely= y, relwidth= 0.15, relheight= 0.3)

    def filmSelectIndex(self, filmIndex):
        self.selectedFilm = filmIndex   
        self.firstWindowLabel.pack_forget()
        self.secondWindow()

    def roomSelectIndex(self, roomIndex):
        if roomIndex == -1 and self.selectedRoom == 0:
            self.selectedRoom = len(self.cineData.rooms)-1
        elif roomIndex == 1 and self.selectedRoom == len(self.cineData.rooms)-1:
            self.selectedRoom = 0
        else:
            self.selectedRoom += roomIndex
        self.firstWindowLabel.pack_forget()
        self.firstWindow()
    
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

    def secondWindow(self):
        self.secondWindowLabel = Label(self.root, image = self.imageBackGround) 
        self.secondWindowLabel.pack(expand=True)
        self.selectedSeats = []
        self.clientInfoEntries()
        self.cancelButtonOperation()
        self.confirmButtonOperation()        
        self.alertLabelOperation()
        self.seatButtons()

    def clientInfoEntries(self):
        filmNameLabel = Label(self.secondWindowLabel, text=self.cineData.rooms[self.selectedRoom].films[self.selectedFilm].nameFilm, bg="black", fg="white", font="robotomono 20 bold", anchor="center")
        filmNameLabel.place(relx=0.39, rely=0.01, relwidth=0.20, relheight=0.035)

        clientNameLabel = Label(self.secondWindowLabel, text="Nome:", bg="black",fg="white",font=("robotomono", 12, "bold"), anchor=W)
        clientNameLabel.place(relx=0.41, rely=0.055, relwidth=0.05, relheight=0.022)
        self.clientNameEntry = Entry(self.secondWindowLabel)
        self.clientNameEntry.place(relx=0.47, rely=0.058, relwidth=0.10, relheight=0.022)

        clientNumberLabel = Label(self.secondWindowLabel, text="Telefone:",bg="black",fg="white",font=("robotomono", 12, "bold"),anchor=W)
        clientNumberLabel.place(relx=0.41, rely=0.083, relwidth=0.06, relheight=0.022)
        self.clientNumberEntry = Entry(self.secondWindowLabel)
        self.clientNumberEntry.place(relx=0.47, rely=0.085, relwidth=0.10, relheight=0.022)

    def cancelButtonOperation(self):
        cancelButton = Button(self.secondWindowLabel, text="Cancelar", bg="red",font=("robotomono", 11, "bold"), anchor="center", command=self.cancelOperation)
        cancelButton.place(relx=0.41, rely=0.12, relwidth=0.06, relheight=0.04)

    def confirmButtonOperation(self):
        confirmButton = Button(self.secondWindowLabel, text="Confirmar", bg="#80ff80",font=("robotomono", 11, "bold"), anchor="center" , command= lambda : self.confirmSeats(self.clientNameEntry.get(), self.clientNumberEntry.get(), self.selectedSeats))
        confirmButton.place(relx=0.51, rely=0.12, relwidth=0.06, relheight=0.04)
    
    def alertLabelOperation(self):
        self.alertLabel = Label(self.secondWindowLabel, bg="black", fg="#ff0000", font=("robotomono", 12, "bold"), anchor="center")
        self.alertLabel.place(relx=0.31, rely=0.17, relwidth=0.35, relheight=0.04)

    def cancelOperation(self):
        self.secondWindowLabel.pack_forget()
        self.firstWindow()

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
            self.secondWindowLabel.pack_forget()
            self.firstWindow()
        


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
        indexSeat = 0
        for i in range(1, 11):
            for j in range(1, 21):
                if j < 11:
                    button = Button(self.secondWindowLabel, text=self.cineData.rooms[self.selectedRoom].films[self.selectedFilm].seats[indexSeat].id, bg="blue", fg="white", font=("robotomono", 10, "bold"), relief=FLAT, command=self.selectSeat)
                    if self.cineData.rooms[self.selectedRoom].films[self.selectedFilm].seats[indexSeat].occupied == True:
                        button["bg"] = "red"
                        button["state"] = "disabled"
                    button["command"] = lambda button=button: self.selectSeat(button["text"],button)
                    button.place(relx= j/46+0.2, rely= i/15+0.2, relwidth=0.020 , relheight=0.04)
                else:
                    button = Button(self.secondWindowLabel, text=self.cineData.rooms[self.selectedRoom].films[self.selectedFilm].seats[indexSeat].id, bg="blue", fg="white", font=("robotomono", 10, "bold"), relief=FLAT, command=self.selectSeat)
                    if self.cineData.rooms[self.selectedRoom].films[self.selectedFilm].seats[indexSeat].occupied == True:
                        button["bg"] = "red"
                        button["state"] = "disabled"
                    button["command"] = lambda button=button: self.selectSeat(button["text"],button)
                    button.place(relx= j/46+0.3, rely= i/15+0.2, relwidth=0.02 , relheight=0.04)
                indexSeat+=1

Application(0, 0)