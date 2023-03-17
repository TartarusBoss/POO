from main.model.main import Carta, Mano


def funcion(p1,p2,p3=10):
    print(f"{p1},{p2},{p3}")

def funcion(nombre, *args, **kwargs):

    for p in args:
        print(p)

    for k, v  in kwargs.items():
        print(f"{k} => {v}")

if __name__ == "__main__":
    carta = Carta("CORAZON", "10")
    mano = Mano()
    funcion("Maria", 20,30,40, p1=1,p2=2,p3=3,p4=4,p5=5,p6=6,p7=7,p8=8, si=True, carta=Carta("CORAZON", "2"))