from tkinter import *
from PIL import ImageTk, Image  

root = Tk()

class Application:
    def __init__(self):
        self.root = root
        self.imgBg = ImageTk.PhotoImage(Image.open("src/assets/imgs/background.png"))
        self.tela()
        self.rooms()
        self.addRoom()
        self.addRoomButton()
        root.mainloop()

    def tela(self):
        self.root.title("Projeto Cinema")
        self.root.geometry("788x988")
        self.root.resizable(True, True)
        self.root.minsize(width=488, height=788)
        self.root.iconbitmap('src/assets/icons/icon.ico')
        label1 = Label(root, image = self.imgBg) 
        label1.place(x=0, y=0, relwidth=1, relheight=1)

    def rooms(self):
        self.frameRooms = Frame(self.root)
        self.frameRooms.place(relx= 0.1, rely= 0.1, relwidth= 0.8, relheight= 0.2)
    def addRoom(self):
        self.frameAddRoom = Frame(self.root)
        self.frameAddRoom.place(relx= 0.1, rely= 0.4, relwidth= 0.8, relheight= 0.2)
    def addRoomButton(self):
        self.btAddRoom = Button(self.frameAddRoom, text="Adicionar")
        self.btAddRoom.place (relx= 0.2, rely = 0.8, relwidth= 0.1, relheight=0.15)


Application()