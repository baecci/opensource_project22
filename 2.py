t, allsum = 10, 1
a=[]

if __name__=="__main__":

    for j in range(0, t):
        a.append(int(input()))
    for i in range(0, t):
        allsum += a[i]
        print("%d] %d" % (i+1, allsum))
    
