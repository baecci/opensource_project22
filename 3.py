#함수 선언 구역   
    

#전역 변수 선언 구역
t = 2
a = []
outa1, outa2 = "", ""
'''
a = ['Open source is source code that is made freely available for possible modification and redistribution.', 'Code is released under the terms of a software license.']
'''
#메인 코드 구역
if __name__=="__main__":
    a.append(input("1번 문자열을 입력하세요: "))
    count1 = len(a[0])

    for i in range(0, count1):
        h = a[0][i]
        if(ord(h)>=ord("a") and ord(h)<=ord("z")):
            nh = h.upper()
        else:
            nh = h

        outa1 += nh

    
    a.append(input("2번 문자열을 입력하세요: "))
    count2 = len(a[1])

    for j in range(0, count2):
        h = a[1][j]
        if(ord(h)>=ord("a") and ord(h)<=ord("z")):
            nh = h.upper()
        else:
            nh = h

        outa2 += nh

    print("1] %s" % outa1)
    print("2] %s" % outa2)
            
