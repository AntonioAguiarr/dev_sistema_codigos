class Transporte:
    def __init__(self, capacidade, velocidade_maxima):
        self.__capacidade = capacidade
        self.__velocidade = velocidade_maxima

    def getCapacidade(self):
        return self.__capacidade
