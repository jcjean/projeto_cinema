class Seat:
    def __init__(self, id):
        self.__id = id
        self.__occupied = False
        self.__owner = ""
        self.__ownerNumber = 0
    
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def occupied(self):
        return self.__occupied

    @occupied.setter
    def occupied(self, occupied):
        self.__occupied = occupied

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, owner):
        self.__owner = owner

    @property
    def ownerNumber(self):
        return self.__ownerNumber

    @ownerNumber.setter
    def ownerNumber(self, ownerNumber):
        self.__ownerNumber = ownerNumber
