import random


class Car:
    def __init__(self, model: str, color: str, fuel_level: float):
        self.model = model
        self.color = color
        self.fuel_level = fuel_level
        self.trip_distance = 0

    def move(self, distance: float):
        """Simulates the movement of the car for a given distance.
        If there is insufficient fuel, the car does not move."""
        is_fuel_enough = distance <= self.fuel_level

        if not is_fuel_enough:
            return

        self.fuel_level -= distance
        self.trip_distance += distance


class Race:
    def __init__(self, cars: list[Car], desired_dist: float):
        self.cars = cars
        self.desired_dist = desired_dist
        self.is_possible = True

    def is_any_car_fueled_enough(self, race_dist: float):
        """Checks if all participating cars have sufficient fuel to start the race.
        Returns True if at least one car has fuel level greater than zero."""
        return any(car.fuel_level >= race_dist for car in self.cars)

    def start_race(self):
        """Initiates the race, simulating the movement of cars until a winner is determined.
        The race continues until one of the cars surpasses or reaches the desired distance.
        The first car to achieve this distance is declared the winner, and the race ends."""
        while self.is_possible:
            race_dist = random.randrange(1, 9)

            # If any car has insufficient fuel to start the race, it prints a message and exits the function.
            if not self.is_any_car_fueled_enough(race_dist) or not self.is_any_car_fueled_enough(self.desired_dist):
                print("У всіх автомобілів недостатньо пального.")
                self.is_possible = False
                return

            for car in self.cars:
                car.move(race_dist)
                if car.trip_distance >= self.desired_dist and self.is_possible:
                    print(f"{car.color} {car.model} виграв гонку! Проїхавши {car.trip_distance} км.")
                    self.is_possible = False

    def show_results(self):
        """Displays the results of the race for each participating car."""
        for auto in self.cars:
            print(f"{auto.color} {auto.model} проїхав {auto.trip_distance} км і має запас палива {auto.fuel_level}.")


car1 = Car("Toyota", "Blue", random.randrange(0, 9))
car2 = Car("Ford", "Yellow", random.randrange(0, 9))
car3 = Car("Honda", "Green", random.randrange(0, 9))

race_instance = Race([car1, car2, car3], 5)
race_instance.start_race()
race_instance.show_results()
