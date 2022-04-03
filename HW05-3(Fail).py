'''''''''''''''''''''''''''''''''''''''''''''''''''
         오픈소스기초프로젝트 5주차 과제

제출: 2022년 4월 3일                     2021041081
                                           배기원
'''''''''''''''''''''''''''''''''''''''''''''''''''
import turtle
import random
import tkinter.simpledialog import *

#함수 구역


#전역 변수 구역
inStr, outStr = '', ''
swidth, sheight = 500, 500
length, textsize, tx, ty = 0, 20, 0, 0  #문자열 길이, 문자 크기, 거북이 좌표 변수 
count = 0  #거북이가 회전한 수

#메인 코드 구역
if __name__=="__main__":
    turtle.title('거북이 회오리')
    turtle.shape('turtle')
    turtle.setup(width=swith+50, height=sheight+50)  #width는 선굵기
    turtle.screensize(swith, sheight)
    turtle.penup()

    inStr=askstring('문자열을 입력하세요', '거북이가 쓸 문자열')

    length=len(inStr)
    angle=360*2/length  #거북이가 한번 회전하는 단위 각도
    turtle.setheading(angle)  #초기 각도를 지정

    for i in inStr:
        angle += 1
        turtle.left(angle)  #현재 각도에서 왼쪽으로 angle도 회전
        nowangle=count*angle  #거북이의 현재 각도=거북이가 회전한 수x단위 각도
        turtle.goto(

https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=python_math&logNo=221214856867
 #참고 자료 #코드 미완     
        

    
