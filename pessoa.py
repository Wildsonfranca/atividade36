#Crie um programa que cria dois objetos da mesma classe (Pessoa), e mostre uma conversa amigável entre os dois objetos.
# NOTE: Definindo a classe Pessoa
class Pessoa:
    def __init__(self, nome, idade, cpf, email):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.email = email

    def falar(self, mensagem):
        return f"{self.nome} diz: {mensagem}"
# Importando a classe Pessoa
from pessoa import Pessoa

#NOTE: Criando duas instâncias da classe Pessoa
pessoa1 = Pessoa("Alice", 28, "111.222.333-44", "alice@example.com")
pessoa2 = Pessoa("Bob", 32, "555.666.777-88", "bob@example.com")

# NOTE:Simulando uma conversa entre as duas pessoas
print(pessoa1.falar("Olá, Bob! Como você está hoje?"))
print(pessoa2.falar("Oi, Alice! Estou bem, obrigado. E você?"))
