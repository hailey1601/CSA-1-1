# Class trong OOP: tạo 1 ra khuôn mẫu bao gồm các thuộc tính và chức năng mà mình tự định nghĩa trong class
# => Các đối tượng sẽ có tính đồng bộ về mặt giá trị và chức năng

class Car:
    def __init__(self, carName: str, carColor: str, carBrand: str, carLongivity: int, income: int, price: int):
        self.carName = carName
        self.carColor = carColor
        self.carBrand = carBrand
        self.carLongivity = carLongivity
        self.income = income
        self.price = price
    
    def printSomething(self):
        print(f"""Oto có màu sắc là: {self.carColor}
Oto thuộc hãng: {self.carBrand}
Oto ra đời được: {self.carLongivity}
              """)
        
    def calculate(self):
        cal = self.income * self.price
        return cal
        

car1 = Car("Honda Civic", "red", "Honda", 30, 10, 5)
car2 = Car("Camry", "Silver", "Toyota", 50, 8, 9)
print(car1.carName)
print(car2.carName)

car1.printSomething()


if car1.calculate() > car2.calculate():
    print(car1.carName)
else:
    print(car2.carName)