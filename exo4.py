t1=[31,28,31,30,31,30,31,31,30,31,30,31]
t2=['janvier','fevrier','mars','avril','mai','juin','juillet','aout','septembre','octobre','novembre','decembre']
'''t3=[]
c1=0
c2=0

for k in range(12):
    
    for i in range(len(t2)) :
        
        d=t2[c1]
        t3.append(d)
        c1+=1
        break

    for j in range(len(t1)) :
        d=t1[c2]
        t3.append(d)
        c2+=1
        break
print(' 1- c\'est la premier question :')
print(t3)
print('2- c\'est la deuxieme question :')
A=[44,99,9,1,0]
B=[]
for i in range(len(A)):
    B.append(0)

A.sort()
d=0
for i in A:

    B[d]=i
    d+=1

print(B)
print('3- c\'est la troisieme question :')
A=[44,99,9,1,0]
B=[]
A.sort()
for i in A:

    B.append(i)

print(B)'''

'''up date de la question 2
t3 = []
for i in range(len(t1)):
    t3.append(t2[i])
    t3.append(t1[i])'''
d=0
for i in range(len(t1)):
   
    t1.insert(i+d,t2[i])
    d+=1

    

print(t1)