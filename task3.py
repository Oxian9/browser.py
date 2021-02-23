class vehicles:
    def __init__(self, number_of_wheels, type_of_tank, seating_capacity, maximum_velocity):
        self.number_of_wheels = number_of_wheels
        self.type_of_tank = type_of_tank
        self.seating_capacity = seating_capacity
        self.maximum_velocity = maximum_velocity

    def drive(self) :
        print("the vehicle is in driving mode now.")

class ElectricCar(vehicles):
    def __init__(self, number_of_wheels, seating_capacity, maximum_velocity) :
        vehicles.__init__(self, number_of_wheels, 'electric', seating_capacity, maximum_velocity)

vios = vehicles ( '4', 'petrol', 5, 180)
print(vios.number_of_wheels)
print(vios.type_of_tank)
print(vios.seating_capacity)
print(vios.maximum_velocity)

blueSG = ElectricCar ( '4', 5, 150)
blueSG.drive()