from d_museum.guia import Guia
from d_museum.turista import Turista

def abrir_museo(turistas=10, guias=5):
    print("Bienvenidos al museo de Dijkstra")

    for j in range(0,guias):
        t = Guia(j)
        t.start()

    for m in range(0,turistas):
        t = Turista(m)
        t.start()