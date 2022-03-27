'''''''''''''''''''''''''''''''''''''''''''''''''''
         오픈소스기초프로젝트 2주차 과제

2022년 3월 27일                     2021041081
                                        배기원
'''''''''''''''''''''''''''''''''''''''''''''''''''
import random

##함수 선언구역


##전역 변수 선언구역
aa=[]
i, j, mini=0, 0, 0

##메인 코드 구역
if __name__=="__main__":
    for i in range(0,5):
        temp=hex(random.randrange(0,100000))
        #temp=hex(int(input("%d번째 10진수를 입력하세요: ", % i+1)))나
        #aa[i]=hex(input("%d번째 10진수를 입력하세요: ", % (i+1))
        #대체 input으로 하면 왜 오류가 생기는 걸까
        aa.append(temp)
                         
    print("정렬 전 리스트: ")
    print(aa)
    print("\n")
                    
    for i in range(0,5):     #가장 앞 인덱스를 최소값이라 정하고 비교하여 선택정렬
        mini=aa[i]
        for j in range(i+1,5):
            if (mini>aa[j]):
                mini=aa[j]
                aa[j]=aa[j-1]
                aa[j-1]=mini
                    
    print("정렬 후 리스트: ")
    print(aa)
            
            
            
    

                    
        
