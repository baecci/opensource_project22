'''''''''''''''''''''''''''''''''''''''''''''''''''
         오픈소스기초프로젝트 5주차 과제

제출: 2022년 4월 3일                     2021041081
                                             배기원
'''''''''''''''''''''''''''''''''''''''''''''''''''

#함수 선언 구역

def changecase(word):  #원래 문자가 대문자로 바꾼 것과 같다면 원래 대문자였다를 이용 
    if(word==word.lower()):
        return word.upper()
    if(word==word.upper()):
        return word.lower()

#전역 변수 선언 구역
length, strarr=0, ''  #문자열 길이 저장할 변수, 문자열 저장할 변수

#메인 코드 구역
if __name__=="__main__":
    strarr=input("문자열을 입력하세요: ")
    length=len(strarr)

    print("\n대소문자 바꾸기 전 문자열: "+strarr)
    print("대소문자 바꾼 후 문자열: ", end='')

    for i in range(0, length):  #문자마다 함수로 전달해 대소문자 바꾸기
        print(changecase(strarr[i]), end='')


