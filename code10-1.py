#함수 선언 구역

#전역 변수 선언 구역

class car():
    speed = 0

    def upspeed(self, value):
        self.speed += value
        if(self.speed>150): self.speed=150

#메인 함수 구역
mycar=car()
value=int(input())
mycar.upspeed(value)
print(mycar.speed)