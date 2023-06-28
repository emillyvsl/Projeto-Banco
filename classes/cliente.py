class Cliente:
    _id=0
    def __init__(self, n, e, cpf):
        self.__num = self.num()
        self.__nome = n
        self.__endereco = e
        self.__CPF = cpf
#Métodos
    @classmethod
    def num(cls):
        cls._id += 1
        return cls._id
    @property
    def numero(self):
        return self.__num

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, value):
        self.__nome = value

    @property
    def endereco(self):
        return self.__endereco

    @endereco.setter
    def endereco(self, value):
        self.__endereco = value

    @property
    def cpf(self):
        return self.__CPF

    @cpf.setter
    def cpf(self, value):
        self.__CPF = value