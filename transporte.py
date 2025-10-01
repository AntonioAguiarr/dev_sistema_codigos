class Veiculo:
    def __init__(self, marca, modelo, cor, ano):
        self.__marca = marca
        self.__modelo = modelo
        self.__cor = cor
        self.__ano = ano
        self.__cores = ['branco','preto', 'cinza', 'vermelho']

    def getMarca(self):
        return self.__marca
    def getModelo(self):
        return self.__ano
    def getCor(self):
        return self.__cor
    def setCor(self, novaCor):
        contagem = 0
        for cor in self.__cores:
            if cor == novaCor:
                contagem = 1
                break
        
        if contagem == 1:
            self.__cor = novaCor
        else:
            print('Cor não alterada.')

    def detalhes(self):
        print(f"Esse carro é da marca {self.__marca}, modelo {self.modelo}, da cor {self.cor} \
              e do ano {self.ano}.")
        
    def acelerar(self):
        print("Acelerando um veículo aleatório.")
        


class Carro(Veiculo):
    def __init__(self, marca, modelo, chassi, placa, cor, ano, portas):
        super().__init__(marca, modelo, chassi, placa, cor, ano)
        self.__portas = portas
    
    def getPortas(self):
        return self.__portas
    
    def acelerar(self):
        print()

        
    
    