'''###############output#########
Brand: Tesla
Model: Model 3
Battery: 100 kWh
##############################'''
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def show_vehicle(self):
        print("Brand:", self.brand)


class Car(Vehicle):
    def __init__(self, brand, model):
        Vehicle.__init__(self, brand)
        self.model = model

    def show_car(self):
        print("Model:", self.model)


class ElectricCar(Car):
    def __init__(self, brand, model, battery):
        Car.__init__(self, brand, model)
        self.battery = battery

    def show_battery(self):
        print("Battery:", self.battery)


ev = ElectricCar("Tesla", "Model 3", "100 kWh")
ev.show_vehicle()
ev.show_car()
ev.show_battery()