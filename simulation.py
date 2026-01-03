import random


class Car:
    def __init__(self, position, velocity=0):
        self.position = position
        self.velocity = velocity


class TrafficSimulation:
    def __init__(
        self,
        road_length=100,
        num_cars=20,
        vmax=5,
        slowdown_prob=0.3,
        seed=42,
    ):
        random.seed(seed)

        self.road_length = road_length
        self.vmax = vmax
        self.slowdown_prob = slowdown_prob
        self.time = 0

        positions = random.sample(range(road_length), num_cars)
        positions.sort()

        self.cars = [Car(pos) for pos in positions]

    def distance_to_next_car(self, index):
        car = self.cars[index]
        next_car = self.cars[(index + 1) % len(self.cars)]

        if next_car.position > car.position:
            return next_car.position - car.position - 1
        else:
            return self.road_length - car.position + next_car.position - 1

    def step(self):
        # 1. Acceleration
        for car in self.cars:
            car.velocity = min(car.velocity + 1, self.vmax)

        # 2. Collision avoidance
        for i, car in enumerate(self.cars):
            gap = self.distance_to_next_car(i)
            car.velocity = min(car.velocity, gap)

        # 3. Random slowdown
        for car in self.cars:
            if car.velocity > 0 and random.random() < self.slowdown_prob:
                car.velocity -= 1

        # 4. Move cars
        for car in self.cars:
            car.position = (car.position + car.velocity) % self.road_length

        self.time += 1

    def average_speed(self):
        return sum(car.velocity for car in self.cars) / len(self.cars)

    def positions(self):
        return [car.position for car in self.cars]
        
    