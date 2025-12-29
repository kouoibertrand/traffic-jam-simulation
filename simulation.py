import random
import matplotlib
matplotlib.use('Agg')  # backend non interactif
import matplotlib.pyplot as plt
import imageio

# ----- Initialisation -----
def initialize_road(length, n_cars, v_max):
    """
    Initialise la route.
    -1 = vide
    1..v_max = vitesse de la voiture
    """
    road = [-1] * length
    positions = random.sample(range(length), n_cars)
    for pos in positions:
        road[pos] = random.randint(1, v_max)
    return road

# ----- Mise à jour -----
def step(road, v_max, p_slow=0.2):
    length = len(road)
    new_road = [-1] * length

    # parcourir la route de la fin vers le début pour éviter écrasements
    for i in reversed(range(length)):
        v = road[i]
        if v != -1:
            # distance jusqu'à la prochaine voiture
            distance = 1
            while distance <= v_max:
                if road[(i + distance) % length] != -1:
                    break
                distance += 1

            vitesse = min(v, distance-1)

            # freinage aléatoire
            if vitesse > 0 and random.random() < p_slow:
                vitesse -= 1

            new_pos = (i + vitesse) % length
            new_road[new_pos] = vitesse

    return new_road

# ----- Visualisation -----
def plot_road(road, v_max, t):
    display = [0 if x == -1 else x for x in road]
    plt.figure(figsize=(10,1))
    plt.imshow([display], cmap='viridis', vmin=0, vmax=v_max, aspect='auto')
    plt.axis('off')
    plt.savefig(f"frame_{t:03d}.png")
    plt.close()

# ----- Simulation -----
if __name__ == "__main__":
    length = 20
    n_cars = 5
    v_max = 3
    p_slow = 0.2
    steps = 20

    road = initialize_road(length, n_cars, v_max)

    # Simuler et sauvegarder les frames
    for t in range(steps):
        road = step(road, v_max, p_slow)
        plot_road(road, v_max, t)

    # Créer le GIF
    frames = [f"frame_{t:03d}.png" for t in range(steps)]
    images = [imageio.imread(f) for f in frames]
    imageio.mimsave("traffic.gif", images, duration=0.1)

    print("Simulation terminée ! GIF généré : traffic.gif")
