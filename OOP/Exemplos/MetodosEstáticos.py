from datetime import date;

class Pessoa:
    def __init__(self,nome,idade) -> None:
        self.nome = nome;
        self.idade = idade;

    @classmethod
    def apartirAnoNascimento(cls,nome,ano):
        return cls(nome,date.today().year - ano);
    #metodo estático para saber se é maior de idade;
    @staticmethod
    def ehMaiorDeIdade(idade):
        return idade >= 18;



pessoa1 = Pessoa('maria',26);

pessoa2 = Pessoa.apartirAnoNascimento('ana',2006);


print(pessoa1.idade);
print(pessoa2.idade);


print(Pessoa.ehMaiorDeIdade(17));