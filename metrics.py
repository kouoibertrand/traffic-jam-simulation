import numpy as np

# ---------------------------
# MÉTRIQUES DE BASE
# ---------------------------

def mean_speed(speeds):
    value = np.mean(speeds)
    print(f"Vitesse moyenne du trafic : {value:.3f}")
    return value


def stopped_fraction(speeds):
    speeds = np.array(speeds)
    value = np.mean(speeds == 0)
    print(f"Fraction de voitures à l'arrêt : {value:.3f}")
    return value


def traffic_flow(num_cars, road_length, speeds):
    mean_v = np.mean(speeds)
    density = num_cars / road_length
    value = density * mean_v
    print(f"Débit du trafic (flow) : {value:.3f}")
    return value


# ---------------------------
# MÉTRIQUES BOUCHONS
# ---------------------------

def mean_stop_duration(speeds):
    durations = []

    for car_speeds in speeds:
        current = 0
        for v in car_speeds:
            if v == 0:
                current += 1
            elif current > 0:
                durations.append(current)
                current = 0
        if current > 0:
            durations.append(current)

    value = np.mean(durations) if durations else 0.0
    print(f"Durée moyenne d'arrêt par événement : {value:.2f} pas de temps")
    return value


def stop_and_go_rate(speeds):
    count = 0
    for car_speeds in speeds:
        for i in range(1, len(car_speeds)):
            if car_speeds[i-1] > 0 and car_speeds[i] == 0:
                count += 1

    value = count / len(speeds)
    print(f"Taux stop-and-go (arrêts / voiture) : {value:.2f}")
    return value


# ---------------------------
# MÉTRIQUES SPATIO-TEMPORELLES
# ---------------------------

def jam_wave_speed(positions, speeds, times):
    jam_points = []

    for i in range(len(speeds)):
        for t in range(len(times)):
            if speeds[i][t] == 0:
                jam_points.append((times[t], positions[i][t]))

    if len(jam_points) < 2:
        print("Vitesse de propagation du bouchon : non détectée")
        return None

    t_vals, x_vals = zip(*jam_points)
    coeffs = np.polyfit(t_vals, x_vals, 1)
    value = coeffs[0]

    print(f"Vitesse de propagation du bouchon : {value:.3f} (dx/dt)")
    return value

def longest_continuous_jam_front(positions, speeds, times):
    """
    Identifie la plus longue séquence temporelle continue
    d'un front arrière de bouchon.
    """

    fronts = []

    for t in range(len(times)):
        stopped_positions = [
            positions[i][t]
            for i in range(len(speeds))
            if speeds[i][t] == 0
        ]
        if stopped_positions:
            fronts.append((times[t], min(stopped_positions)))
        else:
            fronts.append(None)

    # extraire les segments continus
    segments = []
    current = []

    for p in fronts:
        if p is not None:
            current.append(p)
        elif current:
            segments.append(current)
            current = []

    if current:
        segments.append(current)

    if not segments:
        return None

    # prendre le plus long
    return max(segments, key=len)
    
def jam_wave_speed_dominant(positions, speeds, times):
    segment = longest_continuous_jam_front(positions, speeds, times)

    if segment is None or len(segment) < 2:
        print("Vitesse du bouchon dominant : non détectée")
        return None

    t_vals, x_vals = zip(*segment)
    value = np.polyfit(t_vals, x_vals, 1)[0]

    print(f"Vitesse du bouchon dominant : {value:.3f} (dx/dt)")
    return value


def mean_jam_size(speeds):
    speeds = np.array(speeds)
    jam_sizes = np.sum(speeds == 0, axis=0)
    value = np.mean(jam_sizes)

    print(f"Taille moyenne des bouchons : {value:.2f} voitures")
    return value