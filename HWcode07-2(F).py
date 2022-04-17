'''''''''''''''''''''''''''''''''''''''''''''''''''
         오픈소스기초프로젝트 7주차 과제-2

제출: 2022년 4월 17일                  2021041081
                                           배기원
'''''''''''''''''''''''''''''''''''''''''''''''''''
#구글링해도 create_line함수 사용법을 모르겠다.

from tkinter import*
from tkinter import messagebox

#함수 선언 구역

def func_linecolor():
    askcolor()
    
def func_linewidth():
    messagebox.showinfo("선 두께 설정", "선 두께(1~10)를 입력하세요")

def clickLeft(event):
    create_line(0,0,...,600,500)

#전역 변수 선언 구역


#메인 코드 구역
if __name__=="__main__":
    window = Tk()
    window.title("그림판")
    window.geometry("600x500")

    mainMenu = Menu(window)
    window.config(menu = mainMenu)
    
    fileMenu = Menu(mainMenu)
    mainMenu.add_cascade(label = "설정", menu = fileMenu)
    fileMenu.add_command(label = "선 색상 설정", command = func_linecolor)
    fileMenu.add_separator()
    fileMenu.add_command(label = "선 두께 설정", command = func_linewidth)

    window.bind("<Button-1>", clickLeft)

    window.mainloop()
