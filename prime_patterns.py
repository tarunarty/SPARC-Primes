import sympy
import matplotlib

def gen_prime(x=10**4):
    temp = sympy.primerange(0,x)
    return list(temp)

def spacing(lis,y):
    final = []
    c = 0
    for i in range(len(lis)):
        if lis[i]==y:
            final.append(c)
            c = 0
        else:
            c+=1

    return final
            
        
primes = gen_prime()
plot = []
i = 0

current = 10
v = 0

#done using counting primes and then checking their belonging range
while False:
    if i==len(primes):
        break
    
    if primes[i]>current:
        if str(primes[i])[:-1] != str(primes[i])[:-1]:
            inc = (primes[i]-primes[i-1]) // 10
            current += (inc+1)*10
            for __ in range(inc):
                plot.append(0)
            v = 1
            continue
        plot.append(v)
        #if v>4: print(current)
        current += 10
        v = 1
        
    else:
        v += 1
        
    i+=1

plot = [0]*(10**3)
for number in range(10**4):
    if number in primes:
        plot[number//10]+=1
# 880, 850 are not present in the ppt
for x in range(len(plot)):
	if plot[x]==3:
		print(x*10)
		




#final ploting data




