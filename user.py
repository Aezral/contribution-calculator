from uuid import uuid4
class User:
    __id: str
    __name: str

    def __init__(self,name:str):
        self.__id = str(uuid4())
        self.__name = name

    def getId(self):
        return self.__id

    def getName(self):
        return self.__name

