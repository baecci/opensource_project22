'''''''''''''''''''''''''''''''''''''''''''''''''''
         오픈소스기초프로젝트 7주차 과제-2

제출: 2022년 4월 17일                  2021041081
                                           배기원
'''''''''''''''''''''''''''''''''''''''''''''''''''

from tkinter import*
from tkinter import ttk

#함수 선언 구역   
    

#전역 변수 선언 구역


#메인 코드 구역
if __name__=="__main__":
    window = Tk()
    window.title("동물 사진 탭")
    window.geometry("600x500")

    sideTab = ttk.Notebook(window)

    #강아지 탭에 사용할 사진과 라벨 구성
    dogTab = ttk.Frame(sideTab)
    sideTab.add(dogTab, text = "강아지")
    dogPhoto = PhotoImage(file = "C:/Users/qorld/Desktop/PythonWorkspace/picture/dog.gif")
    dogLabel = Label(dogTab, image = dogPhoto)

    #고양이 탭에 사용할 사진과 라벨 구성 
    catTab = ttk.Frame(sideTab)
    sideTab.add(catTab, text = "고양이")
    catPhoto = PhotoImage(file = "C:/Users/qorld/Desktop/PythonWorkspace/picture/cat.gif")
    catLabel = Label(catTab, image = catPhoto)

    #탭과 사진라벨 출력 
    sideTab.pack()
    dogLabel.pack()
    catLabel.pack()

    window.mainloop()
    
