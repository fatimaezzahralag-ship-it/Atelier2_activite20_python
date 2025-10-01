#1
def F1(n):
    m=input('entrer une chaine de caractere :')
    for i in range(n):
        print(m)

F1(5)
#2
def F2(n):
    if (n%10==0):
        print('est divisible par 10')
    else:
        print('n\' est pas divisible par 10')
    
F2(60)
#3
def F3(n):
    p=1
    for i in range(1,n+1):
        p*=i
    return p

print(F3(3))
#4
def F4(n):
    c=0
    
    for lettre in n.lower() :
        if(lettre=='a'or lettre=='o'or lettre=='u'or lettre=='e'or lettre=='y'or lettre=='i'):
            c+=1
    return c

print(F4('EEEEhellOo'))
        
#5

def F5(n):
    for i in range(10):
        print(f"{i}x{n}={i*n}")
    print()
 
F5(5)
#6
def F6(n):
    c=0
    for caractere in n :
        if caractere!=' ':

             c+=1
    print(c)

F6('a b c d ')
#7 LA suite de fibonacci // F(0)=0 , F(1)=1 , POUR n>=2 : F(n)=F(n-1)+F(n-2)
def F7(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    
    else:
        return F7(n-1)+F7(n-2)

    

print(F7(9))


