import random
import time

class SimuladorVida:
    def __init__(self, nome):
        self.nome = nome
        self.fome = 50
        self.energia = 50
        self.felicidade = 50

    def alimentar(self):
        self.fome -= random.randint(5, 15)
        if self.fome < 0:
            self.fome = 0
        print(f"{self.nome} foi alimentado.")

    def dormir(self):
        self.energia += random.randint(10, 20)
        if self.energia > 100:
            self.energia = 100
        print(f"{self.nome} dormiu e recuperou energia.")

    def brincar(self):
        self.felicidade += random.randint(5, 15)
        if self.felicidade > 100:
            self.felicidade = 100
        print(f"{self.nome} brincou e ficou feliz.")

    def status(self):
        print(f"Nome: {self.nome}")
        print(f"Fome: {self.fome}/100")
        print(f"Energia: {self.energia}/100")
        print(f"Felicidade: {self.felicidade}/100")

    def viver(self):
        while True:
            print("\nO que você quer fazer?")
            print("1. Alimentar")
            print("2. Dormir")
            print("3. Brincar")
            print("4. Ver Status")
            print("5. Sair")

            escolha = input("Escolha uma ação: ")

            if escolha == '1':
                self.alimentar()
            elif escolha == '2':
                self.dormir()
            elif escolha == '3':
                self.brincar()
            elif escolha == '4':
                self.status()
            elif escolha == '5':
                print("Saindo do jogo...")
                break
            else:
                print("Escolha inválida. Tente novamente.")

            time.sleep(1)
            self.fome += random.randint(1, 5)
            self.energia -= random.randint(1, 5)
            self.felicidade -= random.randint(1, 5)

            if self.fome >= 100 or self.energia <= 0 or self.felicidade <= 0:
                print(f"{self.nome} morreu devido a maus cuidados. Fim de jogo.")
                break

nome_personagem = input("Digite o nome do seu personagem: ")
simulador = SimuladorVida(nome_personagem)

simulador.viver()
