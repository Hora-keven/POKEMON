import random
import time

import pokemons
Pokemons = pokemons
import inquirer


class Jogo:
    def __init__(self):
        self.menu()
        self.Charmeleon = Pokemons.Pokemon_fogo("Charmeleon", 64, 80, 120)
        self.Wartortle = Pokemons.Pokemon_agua("Wartortle", 63, 58, 120)
        self.Venusaur = Pokemons.Pokemon_planta("Venusaur", 82, 80, 120)
        self.inicio_jogo()

    def dano(self):
        dano_critico = 30
        dano_moderado = 20
        dano_facil = 10
        self.dano_de_vida = [dano_critico, dano_moderado, dano_facil]
        escolha_dano = random.choice(self.dano_de_vida)

        if escolha_dano == 10:
            print("O dano aplicado foi nivel fácil!!")
        elif escolha_dano == 20:
            print("O dano aplicado foi nivel Moderado!!")
        else:
            print("O dano aplicado foi nivel critico!")

        return escolha_dano

    def menu(self):
        print("--------------BATALHA POKEMON-------------")
        print("----------------------ESCOLHA UM POKEMON----------------\n"
              "\033[32mVenusaur - Planta - Vida: 120\033[m\n"
              "\033[31mCharmeleon - Fogo - Vida: 120\033[m\n"
              "\033[34mWartortle - Água - Vida: 120\033[m\n")


    def inicio_jogo(self):

        self.lista = [self.Venusaur.nome, self.Wartortle.nome, self.Charmeleon.nome]
        self.computador = random.choice(self.lista)
        print(self.computador)

        questions = [
            inquirer.List('pokemon',
                          message="Qual pokemon?",
                          choices=[*self.lista],
                          ),
        ]
        poke = inquirer.prompt(questions)
        self.usuario = poke['pokemon']
        lista = ["usuario", "computador"]
        self.escolha_inicio = random.choice(lista)

        self.ambos()

    def ataque_incial(self):

        if self.computador == self.Charmeleon.nome and self.usuario == self.Wartortle.nome:
            self.Charmeleon.vida -= (self.dano() * 2)

            print(f"O usuário{self.usuario} atacou! {self.Charmeleon.nome} tenho {self.Charmeleon.vida} de vida! ")
            self.ataque_computador()

        elif self.computador == self.Charmeleon.nome and self.usuario == self.Venusaur.nome:
            self.Venusaur.vida -= (self.dano() * 2)

            print(f"O computador {self.computador} atacou! {self.usuario} tem {self.Venusaur.vida} de vida! ")
            self.ataque_usuario()

        elif self.computador == self.Venusaur.nome and self.usuario == self.Wartortle.nome:
            self.Wartortle.vida -= (self.dano() * 2)

            print(f"O computador {self.computador} atacou! {self.usuario} tem {self.Wartortle.vida} de vida!")
            self.ataque_usuario()

        elif self.usuario == self.Charmeleon.nome and self.computador == self.Wartortle.nome:
            self.Charmeleon.vida -= (self.dano() * 2)

            print(f"O computador {self.computador} atacou! {self.usuario} tem {self.Charmeleon.vida} de vida! ")
            self.ataque_usuario()

        elif self.usuario == self.Venusaur.nome and self.computador == self.Wartortle.nome:
            self.Wartortle.vida -= (self.dano() * 2)

            print(f"O usuário {self.usuario} atacou! {self.computador} tem {self.Wartortle.vida} de vida!")
            self.ataque_computador()

        elif self.computador == self.Venusaur.nome and self.usuario == self.Charmeleon.nome:
            self.Venusaur.vida -= (self.dano() * 2)

            print(f"O usuário {self.usuario} atacou! {self.computador} tem {self.Venusaur.vida} de vida!")
            self.ataque_computador()

        else:
            print("Escolha um Pokemon certo!")
            self.inicio_jogo()
        self.inicio_jogo()

    def ataque_usuario(self):
        print("--" * 30)
        escolha_ataque = int(input("[1] Ataque\n[2] parar\n"))
        if escolha_ataque == 1:
            if self.computador == self.Charmeleon.nome:
                self.Charmeleon.vida -= self.dano()
                print(
                    f"Agora quem atacou foi o usuário {self.usuario}, computador {self.computador} tem {self.Charmeleon.vida}")

            elif self.computador == self.Venusaur.nome:
                self.Venusaur.vida -= self.dano()
                print(
                    f"Agora quem atacou foi o usuário {self.usuario}, o computador {self.computador} tem {self.Venusaur.vida}")

            elif self.computador == self.Wartortle.nome:
                self.Wartortle.vida -= self.dano()
                print(
                    f"Agora quem atacou foi o usuário {self.usuario}, o computador {self.computador} tem {self.Wartortle.vida}")

            elif escolha_ataque == 2:
                print("Até a próxima batahlha!")
                quit()

        else:
            print("Escreva uma opção certa!")
            self.ataque_usuario()

        self.verifica_ganhador()
        self.ataque_computador()

    def ataque_computador(self):
        print("--" * 30)
        for i in range(2, -1, -1):
            print(f"{self.computador} atacando em {i+1}")
            time.sleep((1))
        print()

        if self.usuario == self.Charmeleon.nome:
            self.Charmeleon.vida -= self.dano()
            print(f"Agora quem atacou foi o computador {self.computador}, {self.usuario} tem {self.Charmeleon.vida}!")

        elif self.usuario == self.Venusaur.nome:
            self.Venusaur.vida -= self.dano()
            print(f"Agora quem atacou foi o computador {self.computador}, {self.usuario} tem {self.Venusaur.vida}!")

        elif self.usuario == self.Wartortle.nome:
            self.Wartortle.vida -= self.dano()
            print(f"Agora quem atacou foi o computador {self.computador}, {self.usuario} tem {self.Wartortle.vida}")

        self.verifica_ganhador()
        self.ataque_usuario()

    def ambos(self):

        if self.usuario == self.Venusaur.nome and self.computador == self.Venusaur.nome:
            if self.escolha_inicio == "computador":
                print("Computador vai atacar primeiro!")
                self.ataque_computador()

            elif self.escolha_inicio == "usuario":
                print("O usuário ataca primeiro!")
                self.ataque_usuario()

        elif self.usuario == self.Wartortle.nome and self.computador == self.Wartortle.nome:
            if self.escolha_inicio == "computador":
                print("Computador vai atacar primeiro!")
                self.ataque_computador()

            elif self.escolha_inicio == "usuario":
                print("O usuário ataca primeiro!")
                self.ataque_usuario()

        elif self.usuario == self.Charmeleon.nome and self.computador == self.Charmeleon.nome:
            if self.escolha_inicio == "computador":
                print("Computador vai atacar primeiro!")
                self.ataque_computador()

            elif self.escolha_inicio == "usuario":
                print("O usuário ataca primeiro!")
                self.ataque_usuario()
        else:
            pass

    def verifica_ganhador(self):

        if self.computador == self.Wartortle.nome and self.Wartortle.vida <=0:
            quit("\033[36[mO usuário ganhou!\033[m")
        elif self.computador == self.Charmeleon.nome and self.Charmeleon.vida <=0:
            quit("\033[36[mO usuário ganhou!\033[m")

        elif self.computador == self.Venusaur.nome and self.Venusaur.vida <= 0:
            quit("\033[36[mO usuário ganhou!\033[m")

        elif self.usuario == self.Wartortle.nome and self.Wartortle.vida <= 0:
            quit("\033[36[mO Computador ganhou!\033[m")

        elif self.usuario == self.Venusaur.nome and self.Venusaur.vida <= 0:
            quit("\033[36[mO Computador ganhou!\033[m")

        elif self.usuario == self.Charmeleon.nome and self.Charmeleon.vida <= 0:
            quit("\033[36[mO Computador ganhou!\033[m")
        else:
            pass


t = Jogo()
t.menu()
