from tkinter import *
from PIL import ImageTk, Image
from HeritageWindow import HeritageWindow


class MainWindow(HeritageWindow):
    def __init__(self, selectedRoom, selectedFilm, cineData):
        super().__init__(cineData)
        self.selectedRoom = selectedRoom
        self.selectedFilm = selectedFilm
        self.imgFilm = []
        self.rooms()
        for i in range(1 , 7):
            if i <= 3:
                self.Films(i/10 * 3, 0.2, i-1, self.cineData.rooms[self.selectedRoom].films[i-1].photoEnd, self.cineData.rooms[self.selectedRoom].films[i-1].dataIni)
            else:
                self.Films((i-3)/10 * 3, 0.6, i-1, self.cineData.rooms[self.selectedRoom].films[i-1].photoEnd, self.cineData.rooms[self.selectedRoom].films[i-1].dataIni)
        self.root.mainloop()

    def rooms(self):
        self.frameRooms = Frame(self.root, bg="black")
        self.frameRooms.place(relx=0.425, rely=0.05, relwidth= 0.1, relheight= 0.05)
        self.labelRooms = Label(self.frameRooms, text=f'{self.cineData.rooms[self.selectedRoom].name}', bg="black",fg="white",font="robotomono 20 bold",anchor="center")
        self.labelRooms.pack(expand=True)

        self.buttonPreviousRoom = Button(self.root, bg="white", fg="black", text="PREVIOUS", font=("robotomono", 13, "bold"), command= lambda: self.selectRoom(-1))
        self.buttonPreviousRoom.place(relx=0.365, rely=0.05, relwidth= 0.07, relheight= 0.04)
        self.buttonNextRoom = Button(self.root, bg="white", fg="black", text="NEXT", font=("robotomono", 14, "bold"), command= lambda: self.selectRoom(1))
        self.buttonNextRoom.place(relx=0.525, rely=0.05, relwidth= 0.06, relheight= 0.04)
        
    def Films(self, x, y, z, photo, data):
        self.frameFilms = Frame(self.root, bg="red")
        self.imgFilm.append(ImageTk.PhotoImage(Image.open(photo).resize([int(self.frameFilms.winfo_screenwidth()*0.15), int(self.frameFilms.winfo_screenheight()*0.3)])))
        labelFilmPhoto = Label(self.frameFilms, image = self.imgFilm[z])
        labelFilmPhoto.pack(expand=True)
        
        labelFilmData = Button(self.root, text=data, bg="black", fg="white", font=("robotomono", 20, "bold"), anchor="center", bd="0", command= lambda: self.selectFilm(z))
        labelFilmData.place(relx= x-0.173, rely= y+0.30, relwidth= 0.1, relheight= 0.05)
        self.frameFilms.place(relx= x-0.2, rely= y, relwidth= 0.15, relheight= 0.3)

    def selectFilm(self, filmIndex):
        self.selectedFilm = filmIndex   
        for widget in self.root.winfo_children():
            widget.destroy()
        from SecondWindow import SecondWindow
        SecondWindow(self.cineData, self.selectedRoom, self.selectedFilm)

    def selectRoom(self, z):
        if z == -1 and self.selectedRoom == 0:
            self.selectedRoom = len(self.cineData.rooms)-1
        elif z == 1 and self.selectedRoom == len(self.cineData.rooms)-1:
            self.selectedRoom = 0
        else:
            self.selectedRoom += z
        for widget in self.root.winfo_children():
            widget.destroy()
        MainWindow(self.selectedRoom, self.selectedFilm, self.cineData)

MainWindow(0, 0, None)