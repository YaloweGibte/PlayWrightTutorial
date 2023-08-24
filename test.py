class Vehicle:
    cnt = 0
    all = []

    def __init__(self, name: str, typ: str, price):
        self.name = name
        self.typ = typ
        self.price = price
        Vehicle.cnt += 1
        Vehicle.all.append(self)

    def clc(self):
        return f"Name: {self.name}\nType: {self.typ}\nType: {self.price}"

    def print_1(self):
        print(f"Name: {self.name} Type: {self.typ} Type:{self.price}")
    def a(self):
        Vehicle.all.append(self)

vehicle_1 = Vehicle("Skoda", "Private", 150000)
vehicle_2 = Vehicle("Ford", "Truck", 450000)
vehicle_3 = Vehicle("Ford", "Truck", 450000)

print(vehicle_1.print_1())
