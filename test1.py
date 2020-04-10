#coding = utf-8


def exam(d, h, m, a):
    h = int(h)
    m = int(m)

    num_d = a // 24*60 
    num_h = (a - num_d) // 60
    num_m = a % 60

    print('whma', w, h, m, a, d)
    print('nh, nm, nd', num_h, num_m, num_d)
    new_h = h - num_h
    new_m = m - num_m
    new_d = new_d - new_d
    print('nt, nm', new_h, new_m)

    t =  { -i:24-i for i in range(0, 24)}



    if new_h < 0:
        new_h = t[new_h]
        if new_m < 0:
            new_h -= 1
            new_m = 60 + new_m
            w -= 1
        elif new_m == 0:
            # new_h -= 1
            w -= 1
    elif new_h == 0:
        new_h = t[new_h] 
        if new_m < 0:
            new_h -= 1
            new_m = 60 + new_m
            w -= 1
        elif new_m == 0:
            new_h =0
            w -= 1
    elif new_h > 0:
        if new_m < 0:
            new_h -= 1
            new_m = 60 + new_m+1
            w -= 1 
        elif new_m == 0:
            pass

    if new_h < 10 :
        new_h = '0'+str(new_h)
    else:
        new_h = str(new_h)

    if new_m < 10:
        new_m = '0'+str(new_m)
    else:
        new_m = str(new_m)

    print(w)
    print(new_h+':'+new_m)





def exam2(n=5, bl=[5, 3, 1, 4, 2], el=[2, 4, 5, 1, 3]):

    pp = 0
    for x in bl:

        back = bl[bl.index(x)+1:]
        front  = bl[:bl.index(x)]
        
        front2 = el[:el.index(x)]
        back2 = el[el.index(x)+1:]
        
        if set(back2) & set(front):
            pp += 1


    print(pp)
            





if __name__ == "__main__":
    while  True:
        try:         
            w = int(input())
            b1 = list(input().split(' '))
            b2 = list(input().split(' '))
            exam2(w, b1, b2)
        except:
            break

