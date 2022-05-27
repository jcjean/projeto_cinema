from Film import Film

class Room:
    def __init__(self, name):
        self.__name = name
        self.__films = list()

    def addFilm(self, name, endPhoto, initData, endData):
        self.__films.append( Film(name, endPhoto, initData, endData))

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def films(self):
        return self.__films

    @films.setter
    def films(self, films):
        self.__films = films
