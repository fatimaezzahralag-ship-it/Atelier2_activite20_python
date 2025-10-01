''''L1=[2,2,9.8,9.7,0]
print(L1[4])
L1[1]=17
L1[3]=(L1[2]+L1[4])
print(L1[4])
print(L1)
L1.reverse()
print(L1)'''


L2=[]
for i in range(4):

    cas=input('tapez 1 si  vous voulez ajouter un entier ou tapez 2 si vous voulez ajouter une chaine de caractere :')
    if cas=='1':

        m=int(  input('entrer un entier :'))
        L2.append(m)
    if cas=='2':
        n=input('entrer une chaine de caractere :')
        L2.append(n)

print(L2)


