class Engine:
    def start(self):
        return "Engine started"
    def stop(self):
        return "Engine stopped"

class Wheels:
    def rotate(self):
        return "Wheels are rotating"

class Car(Engine, Wheels):
    pass

my_car = Car()

print(my_car.start())
print(my_car.rotate())