adresses_ip=["192.168.0.1","10.0.0.1","172.16.0.1","200.100.50.1","169.254.0.1"]
classses_ip={
    "192.168.0.1":"classe A",
    "10.0.0.1":"classe B",
    "172.16.0.1":"classe C",
    "200.100.50.1":"adress ip publique",
    "169.254.0.1":"adresse ip de lien local (apipa)"
}


print(adresses_ip[0]) # affiche la premiere add
print(adresses_ip[-1]) # affiche la derniere add
print(adresses_ip[2]) # affiche le troisieme add

adresses_ip.append("172.31.0.1") # ajoute une nouvelle adresse au tableau
print(adresses_ip)
adresses_ip.remove("200.100.50.1")# supprime l'adresse 200.100.50.1 du tableau
print(adresses_ip)
print('le nombre d\'addresse restants est :',len(adresses_ip))#affiche le nombre des addresse restantes

#qestion 7:
if "192.168.0.1" in adresses_ip:
    print("192.168.0.1 est dans la liste")
else:
    print("192.168.0.1 n\'est pas dans la liste")

print(classses_ip["10.0.0.1"])

valeurs_triees = sorted(classses_ip.keys())#trie les valeurs par ordre alphabetique
print(valeurs_triees)



toutes_classe_C = True
for ip in adresses_ip:
    if classses_ip.get(ip) != "classe C": #get:Python permet de récupérer la valeur associée à une clé.
        toutes_classe_C = False
        break
print(toutes_classe_C)



d=0
for cle , values in classses_ip.items():
   if values== "adress ip publique":
       d+=1
    
print(d)


