import numpy as np
import matplotlib.pyplot as plt
def allel(_size, maxdev):
#     points=np.linspace(0,10,_size)
    points=np.array(range(_size))
    l=np.zeros(_size)
    res=0

    for i in range(1,len(points)):
        dev=np.random.uniform(-1,1)/maxdev
        if l[i-1]>=1:
            l[i]=1
            res=1
        elif l[i-1]<=-1:
            l[i]=-1
            res=-1
        else:
            l[i]=l[i-1]+dev
    return points, l, res

def main():
    num=10
    plus=minus=neutral=0
    for i in range(num):
        f=allel(100,10)
        if f[2]==1:
            plus+=1
        if f[2]==-1:
            minus+=1
        if f[2]==0:
            neutral+=1

        plt.plot(f[0],f[1])

# print (type(plt))
    plt.show()
    print ('Plus={}, Minus={}, Neutral={}'.format(plus,minus, neutral))
if __name__ == '__main__':
    main()
