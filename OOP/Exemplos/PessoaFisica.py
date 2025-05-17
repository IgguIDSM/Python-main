from Pessoa import Pessoa;

class PessoaFisica(Pessoa):
    def __init__(self,cpf, nome, idade):
        super().__init__(nome, idade)
        self.CPF = cpf;

    def setCPF(self,cpf):
        self.CPF = cpf;

    def getCPF(self):
        return self.CPF;