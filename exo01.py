

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


