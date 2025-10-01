machines={
    "m1":"192.168.0.1",
    "m2":"192.168.0.2",
    "m3":"192.168.0.3",
    "m4":"192.168.0.4",
    "m5":"192.168.0.5"
    
}

print(machines["m2"])
print(len(machines))
machines["m6"]="192.168.0.6"
print(machines)
machines.pop("m4")
print(machines)



#exo5:
l=input("entrer le  nom de la machine :")
if l in machines:
    print("l'adresse IP de la machine est :")
    print(machines[l])
else:
    print("la machine n'existe pas")
