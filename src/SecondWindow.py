from tkinter import *
from PIL import ImageTk, Image
from HeritageWindow import HeritageWindow

class SecondWindow(HeritageWindow):
    def __init__(self, cineData, selectedRoom=0, selectedFilm=0):
        super().__init__(cineData)
        self.selectedRoom = selectedRoom
        self.selectedFilm = selectedFilm
        self.selectedSeats = []
        self.infos()
        self.btCancelar()
        self.btConfirmar()
        self.seatButtons()
        self.lbAlert()
        self.root.mainloop()


    def infos(self):
        label1 = Label(self.root, text=self.cineData.rooms[self.selectedRoom].films[self.selectedFilm].nameFilm, bg="black", fg="white", font="robotomono 22 bold", anchor="center")
        label1.place(relx=0.40, rely=0.01, relwidth=0.15, relheight=0.035)

        label2 = Label(self.root, text="Nome:", bg="black",fg="white",font=("robotomono", 12, "bold"), anchor=W)
        label2.place(relx=0.40, rely=0.055, relwidth=0.05, relheight=0.022)
        self.nomeCliente = Entry(self.root)
        self.nomeCliente.place(relx=0.45, rely=0.055, relwidth=0.10, relheight=0.022)

        label3 = Label(self.root, text="Telefone:",bg="black",fg="white",font=("robotomono", 12, "bold"),anchor=W)
        label3.place(relx=0.40, rely=0.083, relwidth=0.05, relheight=0.022)
        self.numeroCliente = Entry(self.root)
        self.numeroCliente.place(relx=0.45, rely=0.083, relwidth=0.10, relheight=0.022)
    
    def btCancelar(self):
        button1 = Button(self.root, text="Cancelar", bg="red",font=("robotomono", 11, "bold"), anchor="center", command=self.cancelOperation)
        button1.place(relx=0.40, rely=0.12, relwidth=0.05, relheight=0.04)

    def btConfirmar(self):
        button2 = Button(self.root, text="Confirmar", bg="#80ff80",font=("robotomono", 11, "bold"), anchor="center" , command= lambda : self.confirmSeats(self.nomeCliente.get(), self.numeroCliente.get(), self.selectedSeats))
        button2.place(relx=0.50, rely=0.12, relwidth=0.05, relheight=0.04)
    
    def lbAlert(self):
        self.alertLabel = Label(self.root, bg="black", fg="#ff0000", font=("robotomono", 12, "bold"), anchor="center")
        self.alertLabel.place(relx=0.40, rely=0.17, relwidth=0.15, relheight=0.04)

    def cancelOperation(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        from MainWindow import MainWindow
        MainWindow(self.cineData, self.selectedRoom, self.selectedFilm)

    def confirmSeats(self, name, number, seats):
        if name == "":
            self.alertLabel["text"] = "Digite o Nome!"
        elif number == "":
            self.alertLabel["text"] = "Digite o Número!"
        elif len(seats) == 0:
            self.alertLabel["text"] = "Necessário pelo menos um assento marcado!"
        else:
            self.cineData.rooms[self.selectedRoom].films[self.selectedFilm].registerSeats(name, number, seats)
            for widget in self.root.winfo_children():
                widget.destroy()
            from MainWindow import MainWindow
            MainWindow(self.cineData, self.selectedRoom, self.selectedFilm)


    def selectSeat(self, id, button):
        if  button["bg"] == "cyan":
            self.selectedSeats.append(id)
            button["bg"] = "orange"
        elif  button["bg"] == "orange":
            for seat in self.selectedSeats:
                if seat == id:
                    self.selectedSeats.remove(seat)
            button["bg"] = "cyan"

    def seatButtons(self):
        a = 0
        for i in range(1, 11):
            for j in range(1, 21):
                if j < 11:
                    button = Button(self.root, text=self.cineData.rooms[self.selectedRoom].films[self.selectedFilm].seats[a].id, bg="cyan", command=self.selectSeat)
                    if self.cineData.rooms[self.selectedRoom].films[self.selectedFilm].seats[a].occupied == True:
                        button["bg"] = "red"
                    button["command"] = lambda button=button: self.selectSeat(button["text"],button)
                    button.place(relx= j/46+0.2, rely= i/15+0.2, relwidth=0.020 , relheight=0.04)
                else:
                    button = Button(self.root, text=self.cineData.rooms[self.selectedRoom].films[self.selectedFilm].seats[a].id, bg="cyan", command=self.selectSeat)
                    if self.cineData.rooms[self.selectedRoom].films[self.selectedFilm].seats[a].occupied == True:
                        button["bg"] = "red"
                    button["command"] = lambda button=button: self.selectSeat(button["text"],button)
                    button.place(relx= j/46+0.3, rely= i/15+0.2, relwidth=0.02 , relheight=0.04)
                a+=1
