class Vehicle:

    def __init__(self, name, max_speed, km_litre):
        self.name = name
        self.max_speed = max_speed
        self.km_litre = km_litre

    def seats_capacity (self, capacity):
        print(f'the max capacity of avaiable seats for vehicle {self.name} are: {capacity}')

    def toStr(self):
        print(f'name = {self.name}')
        print(f'max speed: {self.max_speed}')
        print(f'kms per litre: {self.km_litre}')


model_car = Vehicle('fusca', 180, 10,)
model_car.toStr()

class Bus(Vehicle):
    def seats_capacity(self, capacity=70):
        return super().seats_capacity(capacity=70)

scholar_bus = Bus('scania', 120, 8)
scholar_bus.toStr()
scholar_bus.seats_capacity()