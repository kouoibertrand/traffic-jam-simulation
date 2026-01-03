import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from simulation import TrafficSimulation


def animate_traffic(steps=200, interval=100):
    sim = TrafficSimulation()

    fig, ax = plt.subplots()
    ax.set_xlim(0, sim.road_length)
    ax.set_ylim(-1, 1)
    ax.set_yticks([])
    ax.set_xlabel("Position on road")
    ax.set_title("Traffic simulation (position & speed)")

    # Initial scatter plot
    scatter = ax.scatter(
        sim.positions(),
        [0] * len(sim.cars),
        c=[car.velocity for car in sim.cars],
        cmap="viridis",
        vmin=0,
        vmax=sim.vmax,
        s=100,
    )

    def update(frame):
        sim.step()

        positions = sim.positions()
        velocities = [car.velocity for car in sim.cars]

        scatter.set_offsets(list(zip(positions, [0] * len(positions))))
        scatter.set_array(velocities)

        ax.set_title(
            f"Traffic simulation — time = {sim.time} | avg speed = {sim.average_speed():.2f}"
        )

        return scatter,

    anim = FuncAnimation(
        fig,
        update,
        frames=steps,
        interval=interval,
        blit=True,
    )

    plt.show()


if __name__ == "__main__":
    animate_traffic()