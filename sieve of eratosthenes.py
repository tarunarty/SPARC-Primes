# for calculating all prime numbers in between 1,n inclusive
def lisPrime(n):
    m=int(pow(n,1/2))+1
    ans=[1]*n
    ans[0]=0
    for x in range(4,n+1,2):
        ans[x-1]=0
    for i in range(1,m+1):
        if ans[i-1]:
            for j in range(2*i,n+1,i):
                ans[j-1]=0
    return ans

n=int(input())
lis=lisPrime(n)
"""for i in range(1,n+1):
    if lis[i-1]:
        print(i)"""
print(lis)
            
        
