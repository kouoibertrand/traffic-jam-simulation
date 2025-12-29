import matplotlib
matplotlib.use('Agg')  # backend non interactif
import matplotlib.pyplot as plt

def plot_road(road, v_max, t):
    """
    Affiche la route avec des couleurs selon la vitesse des voitures.
    -1 = vide, 0..v_max = vitesse
    """
    # convertir -1 en 0 pour affichage
    display = [0 if cell == -1 else cell for cell in road]

    plt.figure(figsize=(10, 1))
    plt.imshow([display], cmap='viridis', vmin=0, vmax=v_max, aspect='auto')
    plt.axis('off')
    plt.savefig(f"frame_{t:03d}.png")
    plt.close()
