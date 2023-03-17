from dataclasses import dataclass, field
from typing import ClassVar, Optional

@dataclass
class Carta:

    PINTAS: ClassVar[list[str]] = ["\u2764\uFE0F","\u2763\uFE0F","\u2766\uFE0F","\u2760\uFE0F",]
    VALORES: ClassVar[list[str]] = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    pinta: str
    valor: str
    tapada: bool = field(default=False, init=False)

    """def __init__(self, pinta: str, valor: str):
        self.pinta: str = pinta
        self.valor: str = valor
        self.tapada: bool = False"""


class Mano:

    def __init__(self, cartas: tuple):
        self.cartas: list[Carta] = []
        self.cartas.extend(cartas)

    def es_blackjack(self) -> bool:
        pass
    def es_veintiuno(self) -> bool:
        pass

class Baraja:

    def __init__(self):
        self.cartas: list[Carta] = []
        for pinta in Carta.PINTAS:
            for valor in Carta.VALORES:
                self.cartas.append(Carta(pinta,valor))
    def revolver(self):
        pass

    def repartir_carta(self, tapada=False) -> Carta:
        pass

    def carta_abierta(self, cartas):
        pass


@dataclass
class Jugador:

    nombre:str
    fichas:int
    mano: Mano = field(default=None, init=False)

    def inicializar_mano(self,cartas:tuple):
        pass

    def plantarse(self, cartas):
        pass


@dataclass
class Casa:
    mano: Mano = field(default=None, init=False)

    def inicializar_mano(self, cartas: tuple):
        pass

    def plantarse(self):
        pass
    
class Blackjack:

    def __init__(self):
        self.apuesta_actual: int = 0
        self.jugador: Optional[Jugador] = None
        self.cupier: Optional[Casa] = None
        self.baraja: Baraja = Baraja()

    def registrar_jugador(self, nombre:str):
        pass

    def iniciar_juego(self, apuesta: int):
        pass