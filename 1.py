t, a, b=10, [], []

if __name__=="__main__":
    print("a리스트 입력")
    for i in range(0, t):
        a.append(int(input()))

    print("b리스트 입력")
    for j in range(0, t):
        b.append(int(input()))

    for n in range(0, 10):
        r=a[n]//b[n]
        e=a[n]%b[n]
        print("%d] %d %d" % (n+1, r, e))

    
