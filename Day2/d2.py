class Vehicle:
    def __init__(self, brand: str, model: str, year: int):
        self.brand = brand
        self.model = model
        self.year = year
    
    def display_info(self):
        print(f"""Ten xe la: {self.brand} Dong xe: {self.model} Nam san xuat la: {self.year}""")

    def calculate_tax(self):
        return 0 

class Car(Vehicle):
    def __init__(self, brand: str, model: str, year: int, seats: int, engine_capacity: int):
        super().__init__(brand, model, year)
        self.seats = seats
        self.engine_capacity = engine_capacity
    
    def calculate_tax(self):
        if self.engine_capacity > 2000:
            return 10000000
        else:
            return 5000000

class Motorbike(Vehicle):
    def __init__(self, brand: str, model: str, year: int, engine_capacity: int):
        super().__init__(brand, model, year)
        self.engine_capacity = engine_capacity

    def calculate_tax(self):
        if self.engine_capacity > 150:
            return 3000000
        else:
            return 1000000

class Truck(Vehicle):
    def __init__(self, brand: str, model: str, year: int, max_load: int):
        super().__init__(brand, model, year)
        self.max_load = max_load
    
    def calculate_tax(self):
        if self.max_load > 5:
            return 15000000
        else:
            return 8000000