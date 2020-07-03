# coding = utf-8

def test(n, m, k):
    l2 = []
    for i in range(n):
        i += 1
        l = [i* (x+1) for x in range(m)]
        l2.append(l)
    
    r = 0
    count = 0
    l3 = []
    for a in l2:
        for b in a:
            l3.append(b)
    
    l3.sort()
    
    return l3[m]
    
    
while True:
    try:
        n, m, k = input().split(' ')
        n = int(n)
        m = int(m)
        k = int(k)
        print(test(n, m, k))
    except:
        break