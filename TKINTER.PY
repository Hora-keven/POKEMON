import random
import time
from tkinter import *
import os
from pokemons import Pokemon

telinha = Tk()
pastaApp = os.path.dirname(__file__)


class Tela:
    def __init__(self):
            self.telinha = telinha
            self.Charmeleon = Pokemon("Charmeleon", 64, 80, 120)
            self.Wartortle = Pokemon("Wartortle", 63, 58, 120)
            self.Venusaur = Pokemon("Venusaur", 82, 80, 120)

            self.tela()
            self.frames()
            self.botao_inicio()
            self.imagem()
            self.labels()
            self.poke_computador()
            telinha.mainloop()

    def tela(self):
        self.telinha.title("Batalha Pokemon")
        self.telinha.configure(background="#FFFFFF")
        self.telinha.resizable(True, True)
        self.telinha.wm_geometry(newGeometry="1920x1080")

    def frames(self):
        self.frame = Frame(self.telinha, bg="red", highlightthickness=0.5, highlightbackground="#4682B4")
        self.frame.place(relx=0.03, rely=0.03, relwidth=0.94, relheight=0.11)

        self.frame_2 = Frame(self.telinha, bg='red', highlightthickness=0.5, highlightbackground="#4682B4")
        self.frame_2.place(relx=0.03, rely=0.17, relwidth=0.94, relheight=0.55)

        self.frame_3 = Frame(self.telinha, bg='red', highlightthickness=0.5, highlightbackground="#4682B4")
        self.frame_3.place(relx=0.03, rely=0.75, relwidth=0.94, relheight=0.15)

    def botao_inicio(self):
        self.botao = Button(self.frame_3, font=("Arial", 13), text="Iniciar partida", command=self.tela2)
        self.botao.place(relx=0.28, rely=0.38, relwidth=0.40)

    def labels(self):

        self.lbStatus = Label(self.frame, font=("Arial", 25), text='-=-=-BATALHA POKEMON-=-=-=-', fg='black', bg='red')
        self.lbStatus.place(relx=0.05, rely=0.25, relwidth=0.90, relheight=0.21)

        self.lb_imagem = Label(self.frame_2, image=self.imgvenusaur, bg='red')
        self.lb_imagem.place(relx=0.09, rely=0.001, relwidth=0.30, relheight=0.90)

        self.informacao_pokemon1 = Label(self.frame_2, font=("Arial", 17), fg="black", text=f"Venusaur, Tipo: Planta\nVida: {self.Venusaur.vida}", bg="red")
        self.informacao_pokemon1.place(relx=0.13, rely=0.8, relwidth=0.20, relheight=0.15)

        self.informacao_pokemon2 = Label(self.frame_2, font=("Arial", 17), fg="black", text=f"Charmeleon, Tipo: Fogo\nVida: {self.Charmeleon.vida}", bg="red")
        self.informacao_pokemon2.place(relx=0.43, rely=0.8, relwidth=0.20, relheight=0.15)

        self.informacao_pokemon3 = Label(self.frame_2, font=("Arial", 17), fg="black", text=f"Wartortle, Tipo: Água\nVida: {self.Wartortle.vida}", bg="red")
        self.informacao_pokemon3.place(relx=0.73, rely=0.8, relwidth=0.20, relheight=0.15)

        self.lb_imagem2 = Label(self.frame_2, image=self.imgcharmeleon, bg='red')
        self.lb_imagem2.place(relx=0.41, rely=0.001, relwidth=0.30, relheight=0.8)

        self.lb_imagem3 = Label(self.frame_2, image=self.imgwartortle, bg='red')
        self.lb_imagem3.place(relx=0.70, rely=0.001, relwidth=0.30, relheight=0.80)

    def imagem(self):
        self.imgvenusaur = PhotoImage(file=pastaApp+"//003_f2.png")
        self.imgcharmeleon = PhotoImage(file=pastaApp+"//005.png")
        self.imgwartortle = PhotoImage(file=pastaApp+"//008.png")

    def tela2(self):
        self.telinha2 = Toplevel()
        self.telinha2.title("Batalha Pokemon")
        self.telinha2.configure(background="#FFFFFF")
        self.telinha2.resizable(True, True)
        self.telinha2.wm_geometry(newGeometry="1920x1080")
        self.frames_tela2()
        self.entrada()
        self.label_tela2()
        self.botao_tela2()
        self.escolha_usuario()
        self.escolha_computador()


    def frames_tela2(self):
        self.tela_frame = Frame(self.telinha2, bg="red", highlightthickness=0.5, highlightbackground="#4682B4")
        self.tela_frame.place(relx=0.03, rely=0.03, relwidth=0.94, relheight=0.11)

        self.tela_frame_2 = Frame(self.telinha2, bg='red', highlightthickness=0.5, highlightbackground="#4682B4")
        self.tela_frame_2.place(relx=0.03, rely=0.17, relwidth=0.45, relheight=0.55)

        self.tela_frame_4 = Frame(self.telinha2, bg='red', highlightthickness=0.5, highlightbackground="#4682B4")
        self.tela_frame_4.place(relx=0.52, rely=0.17, relwidth=0.45, relheight=0.55)

        self.tela_frame_3 = Frame(self.telinha2, bg='red', highlightthickness=0.5, highlightbackground="#4682B4")
        self.tela_frame_3.place(relx=0.03, rely=0.75, relwidth=0.94, relheight=0.15)

    def entrada(self):
        self.entrada_usuario = Entry(self.tela_frame_3)
        self.entrada_usuario.place(relx=0.15, rely=0.20, relwidth=0.20, relheight=0.21)

    def label_tela2(self):
            self.lb_escolha_img = Label(self.tela_frame_2, image="",  bg="red")
            self.lb_escolha_img.place(relx=0.25, rely=0.07, relwidth=0.55, relheight=0.80)

            self.lb_escolha_computador = Label(self.tela_frame_4, image="",  bg="red")
            self.lb_escolha_computador.place(relx=0.25, rely=0.05, relwidth=0.55, relheight=0.80)

            self.informacao_poke_computador = Label(self.tela_frame_4, font=("Arial", 17), fg="black", text="", bg="red")
            self.informacao_poke_computador.place(relx=0.43, rely=0.9, relwidth=0.3, relheight=0.15)

            self.informacao_pokemon2_tela2 = Label(self.tela_frame_2, font=("Arial", 17), fg="black", text="", bg="red")
            self.informacao_pokemon2_tela2.place(relx=0.40, rely=0.90, relwidth=0.3, relheight=0.15)

            self.lb_situacao = Label(self.tela_frame, font=("Arial", 15), text="", background='red', fg="black")
            self.lb_situacao.place(relx=0.10, rely=0.05, relwidth=0.75, height=100)

            self.lb_situacao_usuario = Label(self.tela_frame_2, font=("Arial", 15), text="", background='red', fg="black")
            self.lb_situacao_usuario.place(relx=0.1, rely=0.02, relwidth=0.75, height=100)

            self.lb_situacao_comp = Label(self.tela_frame_4, font=("Arial", 15), text="", background='red', fg="black")
            self.lb_situacao_comp.place(relx=0.1, rely=0.02, relwidth=0.75, height=101)

            self.lb_titulo = Label(self.tela_frame, font=("Arial", 25), text="=-BATALHA POKEMON-=", background='red')
            self.lb_titulo.place(relx=0.35, rely=0.05, relwidth=0.25, relheight=0.25)

            self.lb_escolha = Label(self.tela_frame_3, font=("Arial", 15), text="Escolha seu Pokemon:", background='red', fg='black')
            self.lb_escolha.place(relx=0.02, rely=0.20, relwidth=0.13, relheight=0.2)

    def botao_tela2(self):
        self.botao_tela2_ = Button(self.tela_frame_3, font=("Arial", 13), text="Ataque inicial", command=self.escolha_usuario)
        self.botao_tela2_.place(relx=0.36, rely=0.21, relwidth=0.10, relheight=0.18)

        self.botao_ataque = Button(self.tela_frame_3, font=("Arial", 13), text="Ataque", command=self.ataque_usuario)
        self.botao_ataque.place(relx=0.81, rely=0.20, relheight=0.18, relwidth=0.10)

        # self.botao_ataque_comp = Button(self.tela_frame_3, font=("Arial", 13), text="Ataque Computador", command=self.ataque_computador)
        # self.botao_ataque_comp.place(relx=0.68, rely=0.20, relheight=0.18, relwidth=0.10)

    def escolha_usuario(self):

            if self.entrada_usuario.get() == self.Venusaur.nome:
                self.lb_escolha_img.config(image=self.imgvenusaur)
                self.informacao_pokemon2_tela2.config(text=f"Venusaur, Tipo: Planta\n")

            elif self.entrada_usuario.get() == self.Charmeleon.nome:
                self.lb_escolha_img.config(image=self.imgcharmeleon)
                self.informacao_pokemon2_tela2.config(text=f"Charmeleon, Tipo: Fogo\n")

            elif self.entrada_usuario.get() == self.Wartortle.nome:
                self.lb_escolha_img.config(image=self.imgwartortle)
                self.informacao_pokemon2_tela2.config(text=f"Wartortle, Tipo: Água\n")

            self.ambos()

    def escolha_computador(self):
        if self.computador == "Venusaur":
            self.lb_escolha_computador.config(image=self.imgvenusaur)
            self.informacao_poke_computador.config(text=f"Venusaur, Tipo: Planta")

        elif self.computador == "Charmeleon":
            self.lb_escolha_computador.config(image=self.imgcharmeleon)
            self.informacao_poke_computador.config(text=f"Charmeleon, Tipo: Fogo")

        elif self.computador == "Wartortle":
            self.lb_escolha_computador.config(image=self.imgwartortle)
            self.informacao_poke_computador.config(text=f"Wartortle, Tipo: Água")

    def ataque_usuario(self):

        if self.computador == self.Charmeleon.nome:
            self.Charmeleon.vida -= self.dano()
            time.sleep(2)
            self.lb_situacao_usuario.config(text=f"Você foi atacado! {self.entrada_usuario.get()}, você tem {self.Charmeleon.vida} de vida")
            self.verifica_ganhador()

        elif self.computador == self.Venusaur.nome:
            self.Venusaur.vida -= self.dano()
            time.sleep(2)
            self.lb_situacao_usuario.config(text=f"Você foi atacado! {self.entrada_usuario.get()}, você tem {self.Venusaur.vida} de vida")
            self.verifica_ganhador()

        elif self.computador == self.Wartortle.nome:
            self.Wartortle.vida -= self.dano()
            self.lb_situacao_usuario.config(text=f"Você foi atacado! {self.entrada_usuario.get()}, você tem {self.Wartortle.vida} de vida")
            time.sleep(2)
            self.verifica_ganhador()

        else:
            self.lb_situacao.config(text="Escreva uma opção certa!")
        self.ataque_computador()

    def ataque_computador(self):
        if self.entrada_usuario.get() == self.Charmeleon.nome:
            self.Charmeleon.vida -= self.dano()
            self.lb_situacao_comp.config(text=f"Fui atacado!  pelo {self.entrada_usuario.get()} eu tenho {self.Charmeleon.vida} de vida!")
            self.verifica_ganhador()

        elif self.entrada_usuario.get() == self.Venusaur.nome:
            self.Venusaur.vida -= self.dano()
            self.lb_situacao_comp.config(text=f"Fui atacado!  pelo {self.entrada_usuario.get()} eu tenho {self.Venusaur.vida} de vida!")
            self.verifica_ganhador()

        elif self.entrada_usuario.get() == self.Wartortle.nome:
            self.Wartortle.vida -= self.dano()
            self.lb_situacao_comp.config(text=f" Fui atacado!  pelo {self.entrada_usuario.get()} eu tenho {self.Wartortle.vida} de vida!")
            self.verifica_ganhador()

        else:
            self.lb_situacao_comp.config(text="ESCREVA ALGO CERTO")

    def ataque_inicial(self):

        if self.computador == self.Charmeleon.nome and self.entrada_usuario.get() == self.Wartortle.nome:
            self.Charmeleon.vida -= (self.dano()*2)
            self.lb_situacao.config(text=f"O usuário {self.entrada_usuario.get()} atacou! {self.Charmeleon.nome} tenho {self.Charmeleon.vida} de vida! ")
            self.ataque_computador()

        elif self.computador == self.Charmeleon.nome and self.entrada_usuario.get() == self.Venusaur.nome:
            self.Venusaur.vida -= (self.dano()*2)
            self.lb_situacao.config(text=f"O computador {self.computador} atacou! {self.entrada_usuario.get()} tem {self.Venusaur.vida} de vida! ")

        elif self.computador == self.Venusaur.nome and self.entrada_usuario.get() == self.Wartortle.nome:
            self.Wartortle.vida -= (self.dano()*2)

            self.lb_situacao.config(text=f"O computador {self.computador} atacou! {self.entrada_usuario.get()} tem {self.Wartortle.vida} de vida!")

        elif self.entrada_usuario.get() == self.Charmeleon.nome and self.computador == self.Wartortle.nome:
            self.Charmeleon.vida -= (self.dano()*2)

            self.lb_situacao.config(text=f"O computador {self.computador} atacou! {self.entrada_usuario.get()} tem {self.Charmeleon.vida} de vida! ")

        elif self.entrada_usuario.get() == self.Venusaur.nome and self.computador == self.Wartortle.nome:
            self.Wartortle.vida -= (self.dano()*2)
            self.lb_situacao.config(text=f"O usuário {self.entrada_usuario.get()} atacou! {self.computador} tem {self.Wartortle.vida} de vida!")
            self.ataque_computador()

        elif self.computador == self.Venusaur.nome and self.entrada_usuario.get() == self.Charmeleon.nome:
            self.Venusaur.vida -= (self.dano()*2)
            self.lb_situacao.config(text=f"O usuário {self.entrada_usuario.get()} atacou! {self.computador} tem {self.Venusaur.vida} de vida!")
            self.ataque_computador()

        else:
            self.lb_situacao.config(text="Escolha um Pokemon certo!")

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

    def poke_computador(self):

        self.lista = [self.Charmeleon.nome, self.Wartortle.nome, self.Venusaur.nome ]
        self.computador = random.choice(self.lista)

        return self.computador

    def verifica_ganhador(self):
        if self.computador == self.Wartortle.nome and self.Wartortle.vida <= 0:
            self.lb_situacao.config(text=f"O usuário {self.entrada_usuario.get()} ganhou!!")

        elif self.computador == self.Venusaur.nome and self.Venusaur.vida <= 0:
            self.lb_situacao.config(text=f"O usuário {self.entrada_usuario.get()} ganhou!!")

        elif self.computador == self.Charmeleon.nome and self.Charmeleon.vida <= 0:
            self.lb_situacao.config(text=f"O usuário {self.entrada_usuario.get()} ganhou!!")

        elif self.entrada_usuario.get() == self.Wartortle.nome and self.Wartortle.vida <= 0:
            self.lb_situacao.config(text=f"O computador {self.computador} ganhou!!")

        elif self.entrada_usuario.get() == self.Charmeleon.nome and self.Charmeleon.vida <= 0:
            self.lb_situacao.config(text=f"O computador {self.computador} ganhou!!")

        elif  self.entrada_usuario.get() == self.Venusaur.nome and self.Venusaur.vida <= 0:
            self.lb_situacao.config(text=f"O computador {self.computador} ganhou!!")

        else:
            pass

    def ambos(self):
        lista = ["usuario", "computador"]
        self.escolha_inicio = random.choice(lista)

        if self.entrada_usuario.get() == self.Venusaur.nome and self.computador == self.Venusaur.nome:
            if self.escolha_inicio == "computador":
                self.lb_situacao.config(text="Computador vai atacar primeiro!")
                self.ataque_computador()

            elif self.escolha_inicio == "usuario":
                self.lb_situacao.config(text="O usuário ataca primeiro!")
                self.ataque_usuario()

        elif self.entrada_usuario.get() == self.Wartortle.nome and self.computador == self.Wartortle.nome:
            if self.escolha_inicio == "computador":
                self.lb_situacao.config(text="Computador vai atacar primeiro!")
                self.ataque_computador()

            elif self.escolha_inicio == "usuario":
                self.lb_situacao.config(text="O usuário ataca primeiro!")
                self.ataque_usuario()

        elif self.entrada_usuario.get() == self.Charmeleon.nome and self.computador == self.Charmeleon.nome:
            if self.escolha_inicio == "computador":
                self.lb_situacao.config(text="Computador vai atacar primeiro!")
                self.ataque_computador()

            elif self.escolha_inicio == "usuario":
                self.lb_situacao.config(text="O usuário ataca primeiro!")
                self.ataque_usuario()
        else:
            self.ataque_inicial()


Tela()
