# Kế thừa trong python

class Employee:
    def __init__(self, name, id, position, salary, experience):
        self.name = name
        self.id = id
        self.position = position
        self.salary = salary
        self.experience = experience

    def sayHello(self):
        print("Hello ha anh")

class Person:
    def __init__(self, joke):
        self.joke = joke

# class con sẽ kế thường toàn bộ thuộc tính và phương thức mà class cha có
class Coder(Employee, Person):
    def __init__(self, name, id, position, salary, experience, knowledgeOfCoding, language, joke):
        Employee.__init__(self, name, id, position, salary, experience)
        Person.__init__(self, joke)
        self.knowledgeOfCoding = knowledgeOfCoding
        self.language = language

    def sayHello(self):
        print("kdkasdkjasdkn")
coder = Coder(1, 2, 3, 4, 5, 6, 7, 8)
coder.sayHello()