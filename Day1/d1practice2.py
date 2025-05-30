#B1
class Employee:
    def __init__(self, name, position) -> None:
        self.name = name
        self.position = position
    
    def say_hi(self):
        print(f"Hi, my name is {self.name}")
    
    def tell_position(self):
        print(f"I am a {self.position}")

john = Employee("John", "Software Engineer")
john.say_hi()
john.tell_position()

#B2
class area_perimeter:
    def __init__(self):
        self.pi = 3.14

        self.rectangleHeight = None
        self.rectangleWidth = None
        self.circleRadius = None
    
    def calculateRectangleArea(self):
        if self.rectangleHeight is not None and self.rectangleWidth is not None:
            self.rectangleArea = self.rectangleHeight * self.rectangleWidth

            return self.rectangleArea
    
    def calculateRectanglePerimeter(self):
        if self.rectangleHeight is not None and self.rectangleWidth is not None:
            self.rectanglePerimeter = (self.rectangleHeight + self.rectangleWidth) * 2

            return self.rectanglePerimeter
        
    def calculateCircleArea(self):
        if self.circleRadius is not None: 
            self.circleArea = self.pi * (self.circleRadius**2)

            return self.circleArea
    
    def calculateCirclePerimeter(self):
        if self.circleRadius is not None: 
            self.circlePerimeter = 2 * self.pi * self.circleRadius

            return self.circlePerimeter
    
    def runner(self):
        chooseShape = input("Shape (rectangle|circle): ").lower()

        if chooseShape == "rectangle":
            self.rectangleHeight = float(input("Height: "))
            self.rectangleWidth = float(input("Width: "))

            perimeter = self.calculateRectanglePerimeter()
            area = self.calculateRectangleArea()
            print(f"""=> Perimeter: {perimeter} 
                  => Area: {area}""")
            
        elif chooseShape == "circle":
            self.circleRadius = float(input("Radius: "))

            perimeter = self.calculateCirclePerimeter()
            area = self.calculateCircleArea()
            print(f"""=> Perimeter: {perimeter} 
                  => Area: {area}""")
        else: 
            print("Invalid!")

calculate = area_perimeter()
calculate.runner()
        

#B3
from datetime import datetime 

class customDate:
    def __init__(self):
        self.now = datetime.now()
    
    def get_date(self):
        return self.now.strftime("%d/%m/%Y")
    
    def get_time(self):
        return self.now.strftime("%H:%M:%S")
    
    def runner(self):
        print(self.get_date())
        print(self.get_time())

now = customDate()
now.runner()


#B4
from datetime import datetime

class dataHandler:
    def format_date(self, date):
        return date.strftime("%d/%m/%Y")
    
    def daysBetween(self, date1,date2):
        result = date2 - date1
        return result.days
    
    def runner(self):
        formatStartDate = self.format_date(startDate)
        formatEndDate = self.format_date(endDate)
        formatDaysBetween = self.daysBetween(startDate, endDate)

        print(f"Start: {formatStartDate}")
        print(f"End: {formatEndDate}")
        print(f"Days between: {formatDaysBetween}")

startDate = datetime(2021,1,1)
endDate = datetime(2022,1,1)
data_handler = dataHandler()
data_handler.runner()
