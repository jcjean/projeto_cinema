from tkinter import *

root = Tk()

class Application:
    def __init__(self):
        self.root = root    
        self.tela()
        self.rooms()
        self.addRoom()
        self.addRoomButton()
        root.mainloop()
    def tela(self):
        self.root.title("Projeto Cinema")
        self.root.configure(background="black")
        self.root.geometry("788x988")
        self.root.resizable(True, True)
        self.root.minsize(width=488, height=788)
    # def tools(self):
    #     self.frameOfTools = Frame(self.root)
    #     self.frameOfTools.place(relx= 0.1, rely= 0.1, relwidth= 0.8, relheight= 0.2)
    def rooms(self):
        self.frameRooms = Frame(self.root)
        self.frameRooms.place(relx= 0.1, rely= 0.1, relwidth= 0.8, relheight= 0.2)
    def addRoom(self):
        self.frameAddRoom = Frame(self.root)
        self.frameAddRoom.place(relx= 0.1, rely= 0.4, relwidth= 0.8, relheight= 0.2)
    def addRoomButton(self):
        self.btAddRoom = Button(self.frameAddRoom, text="Adicionar")
        self.btAddRoom.place (relx= 0.2, rely = 0.8, relwidth= 0.1, relheight=0.15)

    # def seats(self):
    #     self.frameSeats = Frame(self.root)
    #     self.frameSeats.place(relx= 0.1, rely= 0.1, relwidth= 0.8, relheight= 0.2)
    # def ownSeat(self):
    #     self.frameOwnSeat = Frame(self.root)
    #     self.frameOwnSeat.place(relx= 0.1, rely= 0.1, relwidth= 0.8, relheight= 0.2)

Application()