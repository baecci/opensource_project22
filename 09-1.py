'''
문자열 암호화/디암호화
'''


#함수 선언 구역


#전역 변수 선언 구역
inFp, outFp, i, secu = None, None, 0, 0
inStr, outStr = "", ""

#메인 함수 구역
if __name__=="__main__":
    secuYN = input("1. 암호화 / 2. 암호 해석: ")

    inFname = input("입력 파일명을 입력하세요: ")
    outFname = input("출력 파일명을 입력하세요: ")

    if secuYN == "1":
        secu = 100
    elif secuYN == "2":
        secu = -100

    inFp = open(inFname, 'r', encoding = 'utf-8')
    outFp = open(outFname, 'w', encoding = 'utf-8')

    while True:
        inStr = inFp.readline()
        if not inStr:
            break

        outStr = ""
        for i in range(0, len(inStr)):
            ch = inStr[i]
            chNum = ord(ch)
            chNum = chNum +secu
            ch2 = chr(chNum)
            outStr = outStr + ch2

        outFp.write(outStr)

    outFp.close()
    inFp.close()
    print("%s-->%s 변환 완료" %(inFname, outFname))

