class Vehicle:
    def __init__(self, year, model):
        self.year = year
        self.model = model

    def display_info(self):
        print(f"year: {self.year}, model: {self.model}")


class VehicleDetails(Vehicle):
    def __init__(self, year, model, brand, color):
        super().__init__(year, model)
        # Vehicle.__init__(self, year, model)
        self.brand = brand
        self.color = color

    def display_details(self):
        self.display_info()
        # Vehicle.display_info()
        print(f"brand: {self.brand}, color: {self.color}")



car = VehicleDetails(2022, "Camry", "Hyundai", "black")
car.display_details()
