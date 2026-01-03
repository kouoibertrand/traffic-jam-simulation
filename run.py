from simulation import TrafficSimulation


def run_simulation(steps=100):
    sim = TrafficSimulation()

    avg_speeds = []

    for _ in range(steps):
        sim.step()
        avg_speeds.append(sim.average_speed())

    return avg_speeds


if __name__ == "__main__":
    speeds = run_simulation(200)
    print("Final average speed:", speeds[-1])