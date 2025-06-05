#B2
class MathList:
    def __init__(self, numberList):
        self.value = list(numberList)
    
    def __str__(self):
        return str(self.value)
    
    def __add__(self, other):
        new_values = []
        for item in self.value:
            new_values.append(item + other)
        
        return MathList(new_values)
    
    def __sub__(self, other):
        new_values = []
        for item in self.value:
            new_values.append(item - other)
        
        return MathList(new_values)
        
m_list= MathList([1, 2, 3, 4, 5])
print(m_list)

m_list += 2
print(m_list)


#B3
class Square:
    def __init__(self, square):
        self.square = square

    def cal_area(self):
        self.squareArea = self.square * self.square 

        return self.squareArea

class Cube(Square):
    def __init__(self, square):
        super().__init__(square)
    
    def cal_area(self):
        return super().cal_area()
    
    def cal_volume(self):
        self.cubeVolume = self.square**3

        return self.cubeVolume

square = Square(2)
print('Square area:', square.cal_area())

cube = Cube(2)
print('Cube area:', cube.cal_area())
print('Cube volume:', cube.cal_volume())

#B4
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    def welcome(self):
        print('Welcome', self.username)
    
    def check_password(self, password_input):
        if password_input == self.password:
            return True
        else:
            return False

from datetime import datetime

class SubscribedUser(User):
    def __init__(self, username, password, date):
        super().__init__(username, password)
        self.date = date
    
    def is_expired(self):
        now = datetime.now()
        if now > self.date:
            return True #het han
        else:
            return False #con han
    
user = User('mindx', '12345')
user.welcome()
print(user.check_password('1234'))

s_user = SubscribedUser('s_mindx', '1234', datetime(2021, 1, 1))
s_user.welcome()
print(s_user.check_password('1234'))
print(s_user.is_expired())