import matplotlib.pyplot as plt
from simulation import TrafficSimulation


def animate_simulation(steps=100):
    sim = TrafficSimulation()

    avg_speeds = []

    for _ in range(steps):
        sim.step()
        avg_speeds.append(sim.average_speed())

    plt.figure()
    plt.plot(avg_speeds)
    plt.xlabel("Time step")
    plt.ylabel("Average speed")
    plt.title("Traffic flow evolution")
    plt.tight_layout()
    plt.savefig("visualization.png", dpi=300)
    plt.close()


if __name__ == "__main__":
    animate_simulation(300)