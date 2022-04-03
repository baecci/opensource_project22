''''''''''''''''''''''''''''''''''''''''''''''''''''
         오픈소스기초프로젝트 2주차 과제

제출: 2022년 4월 3일                      2021041081
                                              배기원
''''''''''''''''''''''''''''''''''''''''''''''''''''
#배운 점: 정수 문자열과 정수or문자열or문자 리스트 등 데이터 형식을 잘 구분해야 한다.

#함수 구역
def onlynum(array):
    global numStr
    for st in array:
        if (st.isdigit==True):
            numStr += st
        else: pass

    return int(numStr)

#전역 변수 구역
num, data, numStr= 0, [], ''  #16진수를 입력받을 문자열 리스트, 숫자만 뽑아내 숫자 문자 리스트를 저장할 numlist
numList = []  #뽑아낸 정수형 숫자를 저장할 리스트

#메인 코드 구역
if __name__=="__main__":
    for i in range(0,5):
        num=int(input("정수를 입력하세요: "))  #정수를 받아 16진수 문자열로 바꾸기
        data.append(hex(num))
    
    for j in range(0,5):
        numList.append(onlynum(data[j]))  #숫자만 골라내어 int형으로 반환

    print("정렬 전: "+numList+"\n")
    
    for a in range(0,4):
        mini=numList[a]
        for b in range(0,4):
            if (mini>numList[b]):
                mini=numList[b]
                numList[b]=numList[a]
                numList[a]=mini

    print("정렬 후: "+numList)

    #코드 미완: 오류 
              
                
        
