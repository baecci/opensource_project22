'''''''''''''''''''''''''''''''''''''''''''''''''''
         오픈소스기초프로젝트 2주차 과제

2022년 3월 27일                     2021041081
                                        배기원
'''''''''''''''''''''''''''''''''''''''''''''''''''
import operator

##함수 선언구역


##전역 변수 선언구역
Tuplelist=[('토마스',8),('헨리',7),('제임스',9),('에밀리',2),('토마스',4),
           ('헨리',12),('토마스',7),('에밀리',8),('퍼시',5),('고든',13)]
trainDic, trainList={}, []
tempTuple=None
cRank, tRank=1, 1

##메인 코드 구역
if __name__=="__main__":
    for tempTuple in Tuplelist:      #튜플을 딕셔너리로 바꾸고 수송량을 누적한다
        Tname=tempTuple[0]      
        Tweight=tempTuple[1]
        if Tname in trainDic:
            trainDic[Tname]+=Tweight
        else:
            trainDic[Tname]=Tweight

    print("기차 수송명단== ", Tuplelist)
    print("____________________________")

    trainList=sorted(trainDic.items(), key=operator.itemgetter(1), reverse=True)
    #순위를 정하기 위한 딕셔너리 정렬
    print("기차\t총수송량\t순위")
    print("----------------------------")
    print(trainList[0][0], '\t', trainList[0][1], '\t', cRank)

    for i in range(1, len(trainList)):  #등수 출력
        tRank+=1
        if trainList[i][1]==trainList[i-1][1]:
            pass
        else:
            cRank=tRank

        print(trainList[i][0], '\t', trainList[i][1], '\t', cRank)
        
