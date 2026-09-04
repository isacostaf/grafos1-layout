import matplotlib.pyplot as plt

# a cidade eh fixa, cada esquina é um no (com cordenadas x,y pra organizar no desenho)
NOS = [
    # linha 0
    {"id": 1, "x": 100, "y": 100},
    {"id": 2, "x": 250, "y": 100},
    {"id": 3, "x": 400, "y": 100},
    # linha 1
    {"id": 4, "x": 100, "y": 250},
    {"id": 5, "x": 250, "y": 250},
    {"id": 6, "x": 400, "y": 250},
]

# tamanho da tela
LAYOUT = {"width": 500, "height": 350}

# ja que a cidade nunca muda as ruas tambem nao
# tem ruas entre todos os nos
RUAS = [
    # ruas horizontais (lado com lado)
    (1, 2), (2, 3),
    (4, 5), (5, 6),
    # ruas verticais (frente com frente)
    (1, 4), (2, 5), (3, 6),
]

if __name__ == "__main__":
    por_id = {no["id"]: no for no in NOS}

    fig, ax = plt.subplots(figsize=(5, 3.5))

    # desenha as ruas (arestas)
    for a, b in RUAS:
        na, nb = por_id[a], por_id[b]
        ax.plot([na["x"], nb["x"]], [na["y"], nb["y"]], color="black", zorder=1)

    # desenha os nos (esquinas)
    for no in NOS:
        ax.scatter(no["x"], no["y"], s=600, color="lightblue", edgecolors="black", zorder=2)
        ax.text(no["x"], no["y"], str(no["id"]), ha="center", va="center", fontweight="bold", zorder=3)

    ax.set_xlim(0, LAYOUT["width"])
    ax.set_ylim(LAYOUT["height"], 0)  # inverte o eixo y pra combinar com o html (y cresce pra baixo)
    ax.set_aspect("equal")
    ax.axis("off")

    plt.savefig("grafo.png")
    plt.show()
