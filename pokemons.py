
class Pokemon:
    def __init__(self, nome : str, ataque : int, velocidade : int, vida : int):
        self.nome = nome
        self.ataque = ataque
        self.velocidade = velocidade
        self.vida = vida


class Pokemon_planta(Pokemon):
    def __init__(self, nome, ataque, velocidade, vida):
        super().__init__(nome, ataque, velocidade, vida)


class Pokemon_fogo(Pokemon):
    def __init__(self, nome, ataque, velocidade, vida):
        super().__init__(nome, ataque, velocidade, vida)

class Pokemon_agua(Pokemon):
    def __init__(self, nome, ataque, velocidade, vida):
        super().__init__(nome, ataque, velocidade, vida)





