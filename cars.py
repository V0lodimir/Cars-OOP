class Cars:
        def __init__(self, speed, color, name, is_police):
            self.speed = speed
            self.color = color
            self.name = name
            self.is_police = is_police

class TownCar(Cars):
    def turn_right(self):
        print ("Car {}, {}, with speed {}, has turned right".format(self.name, self.color, self.speed))
class SportCar(Cars):
    def turn_left(self):
        print ("Car {}, {}, with speed {}, has turned left".format(self.name, self.color, self.speed))
class WorkCar(Cars):
    def stop(self):
        print ("Car {}, {}, with speed {}, has stoped".format(self.name, self.color, self.speed))
class PoliceCar(Cars):
    def go(self):
        print ("Car {}, {}, with speed {}, has go".format(self.name, self.color, self.speed))

town_car = TownCar("70", "White", "Lada", False)
sport_car = SportCar("105", "Green", "Zhugul", False)
work_car = WorkCar("90", "Blue", "Reno", False)
police_car = PoliceCar("100", "Red", "Toyota", True)

town_car.turn_right()
sport_car.turn_left()
work_car.stop()
police_car.go()