from simulation import TrafficSimulation
import matplotlib.pyplot as plt



def collect_trajectories(simulation, steps):
    """
    Collecte les positions et vitesses de chaque voiture à chaque pas de temps.
    
    :param simulation: instance de TrafficSimulation
    :param steps: nombre de pas de temps à simuler
    :return: positions, vitesses
             positions[i][t] = position de la voiture i au temps t
             speeds[i][t] = vitesse de la voiture i au temps t
    """
    positions = [[] for _ in range(len(simulation.cars))]
    speeds = [[] for _ in range(len(simulation.cars))]

    for _ in range(steps):
        simulation.step()
        for i, car in enumerate(simulation.cars):
            positions[i].append(car.position)
            speeds[i].append(car.velocity)

    return positions, speeds
    
def plot_space_time(steps=200):
    sim = TrafficSimulation()
    positions, speeds = collect_trajectories(sim, steps)
    times = list(range(steps))
    
    plt.figure(figsize=(10, 6))
    
    for i in range(len(sim.cars)):
        plt.scatter(times, positions[i], c=speeds[i], s=10, cmap='viridis')
    plt.xlabel("Time")
    plt.ylabel("Position on road")
    plt.title("Space–Time Diagram of Traffic")
    plt.tight_layout()
    plt.savefig("space_time_diagram.png", dpi=300)
    plt.close()



if __name__ == "__main__":
    plot_space_time()