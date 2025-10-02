#7 LA suite de fibonacci // F(0)=0 , F(1)=1 , POUR n>=2 : F(n)=F(n-1)+F(n-2)
def F7(n):
    if n==0:
        return 
    elif n==1:
        return 1
    
    else:
        return F7(n-1)+F7(n-2)

    

print(F7(9))