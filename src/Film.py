from Seat import Seat

class Film:
    def __init__(self, nameFilm, photoEnd, dataIni, dataEnd):
        self.__seats = list()
        for i in range(26):
            for j in range(9):
                self.__seats.append( Seat(f'{ord("A") + i}' + f"{j}"))
        self.__nameFilm = nameFilm
        self.__photoEnd = photoEnd
        self.__dataIni = dataIni
        self.__dataEnd = dataEnd
    
    @property
    def nameFilm(self):
        return self.__nameFilm

    @nameFilm.setter
    def nameFilm(self, nameFilm):
        self.__nameFilm = nameFilm
    
    @property
    def photoEnd(self):
        return self.__photoEnd

    @photoEnd.setter
    def photoEnd(self, photoEnd):
        self.__photoEnd = photoEnd
    
    @property
    def dataIni(self):
        return self.__dataIni

    @dataIni.setter
    def dataIni(self, dataIni):
        self.__dataIni = dataIni
    
    @property
    def dataEnd(self):
        return self.__dataEnd

    @dataEnd.setter
    def dataEnd(self, dataEnd):
        self.__dataEnd = dataEnd