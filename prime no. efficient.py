#efficient version
#check with 2147483647

while True:
    a = int(input())
    b = round(a**(1/2))
    c = 0

    if a==1:
        print("neither prime nor composite")
        c=1
    elif a==2:
        print(a , "is a prime")
        c=1
    else:
        if a%2==0:
            print(a , "is not a prime")
            c=1
        else:
            for i in range(3,b+1,2):
                if a%i == 0:
                    print(a , "is not a prime")
                    c=1
                    break
                
    if c!=1:
        print(a,"is a prime")
   
            
        

        

    
