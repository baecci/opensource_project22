'''''''''''''''''''''''''''''''''''''''''''''''''''
         오픈소스기초프로젝트 7주차 과제-1

제출: 2022년 4월 17일                  2021041081
                                           배기원
'''''''''''''''''''''''''''''''''''''''''''''''''''
### 다 잘되는데 사진 출력이 안되는 문제가 있음. 

from tkinter import* 

#함수 선언 구역

def vote_animal():
    button1.pack()

def show_animal():
    global num 
    if var.get() == 1:
        num = 0
        photo = PhotoImage(file = "C:/Users/qorld/Desktop/PythonWorkspace/picture/"+animalList[num])
        label2.configure(image = photo)
        label2.pack()
    elif var.get() == 2:
        num = 1
        photo = PhotoImage(file = "C:/Users/qorld/Desktop/PythonWorkspace/picture/"+animalList[num])
        label2.configure(image = photo)
        label2.pack()
    else :
        num = 2
        photo = PhotoImage(file = "C:/Users/qorld/Desktop/PythonWorkspace/picture/"+animalList[num])
        label2.configure(image = photo)
        label2.pack()

#전역 변수 선언 구역
animalList=["dog.gif", "cat.gif", "rabbit.gif"]
num = 0

#메인 코드 구역
if __name__=="__main__":
    window = Tk()
    window.title("동물 투표하기")
    window.geometry("600x500")

    label1 = Label(window, text = "좋아하는 동물 투표", font = (25), fg = "blue")
    button1 = Button(window, text = "사진보기", font = (5), fg = "black", command = show_animal)

    var = IntVar()
    dogRB = Radiobutton(window, text = "강아지", variable = var, value = 1, command = vote_animal) 
    catRB = Radiobutton(window, text = "고양이", variable = var, value = 2, command = vote_animal)
    rabbitRB = Radiobutton(window, text = "토끼", variable = var, value = 3, command = vote_animal)

    label1.pack()
    dogRB.pack()
    catRB.pack()
    rabbitRB.pack()

    photo = PhotoImage(file = "C:/Users/qorld/Desktop/PythonWorkspace/picture/"+animalList[num])
    label2 = Label(window, image = photo)
    
    window.mainloop()
    
