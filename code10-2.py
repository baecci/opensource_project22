class Car:
    speed = 0
    def upSpeed(self, value):
        self.speed += value

class Sedan(Car):
    speed = 0

    def upSpeed(self, value):
        self.speed += value
        if(self.speed>150): self.speed = 150

class Sonata(Sedan):
    speed = 0

    def upSpeed(self, value):
        self.speed += value
        if(self.speed>150): self.speed = 150

Car1 = Car()
Car2 = Sedan()
Car3 = Sonata()

value = int(input())
Car1.upSpeed(value)
Car2.upSpeed(value)
Car3.upSpeed(value)

print("Car의 속도: %d\n" %Car1.speed)
print("Sedan의 속도: %d\n" %Car2.speed)
print("Sonata의 속도: %d\n" %Car3.speed)