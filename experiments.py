from simulation import TrafficSimulation
from space_time import collect_trajectories
from metrics import *

STEPS = 300

sim = TrafficSimulation()
positions, speeds = collect_trajectories(sim, STEPS)

times = list(range(STEPS))
num_cars = len(sim.cars)
road_length = sim.road_length

print("\n===== ANALYSE DU TRAFIC =====\n")

mean_speed(speeds)
stopped_fraction(speeds)
traffic_flow(num_cars, road_length, speeds)

print("\n--- BOUCHONS ---\n")

mean_stop_duration(speeds)
stop_and_go_rate(speeds)

print("\n--- SPATIO-TEMPOREL ---\n")

jam_wave_speed(positions, speeds, times)
jam_wave_speed_dominant(positions, speeds, times)
mean_jam_size(speeds)

print("\n============================\n")