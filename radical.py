def issimple(n):
    nums=range(2,int(n**0.5+1))
    for num in nums:
        if n%num==0:
            return False
    return True
def prime_factorization(N):
    #nums=dict {value:power}
    nums={}
    values=range(2,int(N**0.5+2))
    for val in values:
        if issimple(val):
            count=0
            while(N%val==0):
                N=N/val
                count+=1
            if count!=0:
                nums[val]=count
    return nums

def radical(N):
    primes=prime_factorization(N)
    rad=1
    for num in primes:
        rad=rad*num
    return rad
