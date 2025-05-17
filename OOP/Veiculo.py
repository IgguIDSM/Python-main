class Veiculo:
    def __init__(self,nome,velMax,KmPorLitro):
        self.nome = nome; #Porque? sei lá, nome é legal;
        self.velMax = velMax;
        self.KmPorLitro = KmPorLitro;

    def toStr(self):
        print(f'Nome do Veículo: {self.nome}');
        print(f'Vel Max: {self.velMax}');
        print(f'Km Por Litro: {self.KmPorLitro}');

class Onibus(Veiculo):
    def __init__(self, nome, velMax, KmPorLitro, Assentos = 70):
        super().__init__(nome, velMax, KmPorLitro)
        self.Assentos = Assentos;
    
    def toStr(self):
        super().toStr()
        print(f'Quantidade de Assentos: {self.Assentos}');
    pass;

#passagem dos objetos em si

car = Veiculo("Gol",200,20);

car.toStr();






on = Onibus('Mercedez',130,7);

on.toStr();