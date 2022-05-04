from Seat import Seat


class Room:
    def __init__(self, nameOfCine):
        self.__seats = list()
        for i in range(26):
            for j in range(9):
                self.__seats.append( Seat(f'{ord("A") + i}' + f"{j}" , False, None, None))
        self.__nameOfCine = nameOfCine