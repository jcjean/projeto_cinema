from Room import Room

class Cine:
    def __init__(self):
        self.__arquivo = open('src/Filmes.txt', 'r')
        self.__rooms = list()
        self.loadrooms()
        print(self.__rooms[1].name)
        

    def loadrooms(self):
        numberRooms = self.__arquivo.readline()
        for i in range(int(numberRooms)):
            self.__rooms.append(Room(self.__arquivo.readline()))
            numberFilms = self.__arquivo.readline()
            for a in range(int(numberFilms)):
                self.__rooms[i].addFilm(self.__arquivo.readline(), self.__arquivo.readline(), self.__arquivo.readline(), self.__arquivo.readline())

Cine()

