L3=[1,2,3,4,5]
print('1-la liste est virticalement:')
for i in L3:
    print(i)
sum=0
for i in L3:
    sum+=i
print('2-la somme est :')
print(sum)

print('3-le produit des elements : ')
p=1
for i in L3[2:5] :
    p*=i
print(p)

print('4-le max et le min de la liste:')
max=L3[0]
min=L3[0]

for i in L3:
    if(max<=i):
        max=i
    if(min>=i):
        min=i

print(f'le max de cette liste est ={max} / le  min de cette liste  est= {min}')
print('5-les multiples de 3:')
for i in L3 :
    if(i%3==0):
        print(i)
print('6-renverser la liste :')
L3.reverse()
print(L3)
        




