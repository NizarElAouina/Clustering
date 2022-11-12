from itertools import combinations
#Ouvrir le fichier contenant le graphe
T=[1]
b=0
for i in T:
    if i<10:
        print(f"fichier {i}")
        graphe = open(f"C:/Users/nizar/Desktop/graphs/heur00{i}.gr")
        p,cep,e,f=graphe.readline().split() #e: nombre de sommets, f: nombre d'aretes
        n=int(e)
        m = int(f)
        d={}
        print(graphe)
        #Stocker le graphe dans un dictionnaire sous la forme {sommet: voisins}
        for line in graphe:
            u,v = line.split()
            if int(u) not in d.keys() and int(v) not in d.keys(): #4 7
                d[int(u)]=[int(v)] #4:7 AND 7:4
                d[int(v)]=[int(u)]
            elif int(u) in d.keys() and int(v) not in d.keys(): #4 7        4 10
                d[int(u)].append(int(v)) #4:7,10   10:4
                d[int(v)]=[int(u)]
            elif int(u) not in d.keys() and int(v) in d.keys():
                d[int(u)]=[int(v)]
                d[int(v)].append(int(u))
            else:
                d[int(u)].append(int(v))
                d[int(v)].append(int(u))
        L=[]
        for i in d.keys():#donone la liste des keys'''
            L.append(i)
        #print(L)'''
        for i in combinations(L,2): #i=(4,7)
            #dict_items = d.items()
            #first_two = list(dict_items)[i[1]:i[2]] donne les i emes premieres clés et valeurs
            u=i[0] #la premiere clé avec sa valeur u=4
            v=i[1] #la deuxieme clé avec sa valeur v=7
            C=[] #Common neighborhood
            N=[] #Non-Common neighborhood
            for x in d[u] : #boucles qui parcourt les valeurs de la premiere clé,
                if x in d[v]:
                    C.append(x)#si elle les trouve dans les valeurs de la deuxieme clé, elle les ajoutes dans C
                else:
                    N.append(x)#sinon elle les mets dans N
            N2=[]
            for x in d[v] :#parcourt les valeurs de la deuxieme clé
                if x in d[u]:
                    continue
                else:
                    N2.append(x)
            N+=N2
            #N.remove(u)
            #N.remove(v)
            N2=[]
            D=C+N#ici commence le calcul du cout de l'ajout
            cout_suppression=0
            count_ajout = 0
            print("===============")
            if i[0] in d[i[1]]:  # calculer le cout de la supression des aretes qui existent déja dans le graphe
                cout_suppression=2*len(C)
                b+=1
                print("cout delete",cout_suppression)
                for j in D:
                    V=d[j]
                    L = D
                    p = set(D).difference(set(V))  # p=[5,6,3,1,8,7,11]
                    for a in V:
                        if a in p:
                            p.remove(a)
                    count_ajout += len(p)
                print("cout ajout",count_ajout)
                o=i[0]
                p=i[1]
                if count_ajout<cout_suppression:
                    continue
                else:
                    with open("C:/Users/nizar/Desktop/graphs/new_file2.txt",'a+') as file:
                        file.write(f"{o}  {p}\n")
                        file.close()
                    d[i[0]].remove(i[1])
                    d[i[1]].remove(i[0])
                    print(cout_suppression)
                    print(count_ajout)
                    print(i)
            else:
                continue

        print("=============")
        #print("C=",C)
        #print("N=",N)
        #print("N2=",N2)
        #print(d.keys)
        #print(d)
        #print("===================")
        #print('cout delete',cout_suppression)
        #print('Cout ajout',count_ajout)
        #print(len(C))
        #print(b) #pour vérifier qu'il ya bien m suppressions, avec m le nombre d'aretes
        #print("Fin du fichier")
        #print('===================================')


    else:
        print(f"fichier {i}")
        graphe = open(f"C:/Users/nizar/Desktop/graphs/heur0{i}.gr")
        p,cep,e,f=graphe.readline().split() #e: nombre de sommets, f: nombre d'aretes
        n=int(e)
        m = int(f)
        d={}
        print(graphe)
        #Stocker le graphe dans un dictionnaire sous la forme {sommet: voisins}
        for line in graphe:
            u,v = line.split()
            if int(u) not in d.keys() and int(v) not in d.keys(): #4 7
                d[int(u)]=[int(v)] #4:7 AND 7:4
                d[int(v)]=[int(u)]
            elif int(u) in d.keys() and int(v) not in d.keys(): #4 7        4 10
                d[int(u)].append(int(v)) #4:7,10   10:4
                d[int(v)]=[int(u)]
            elif int(u) not in d.keys() and int(v) in d.keys():
                d[int(u)]=[int(v)]
                d[int(v)].append(int(u))
            else:
                d[int(u)].append(int(v))
                d[int(v)].append(int(u))
        L=[]
        for i in d.keys():#donone la liste des keys'''
            L.append(i)
        #print(L)'''
        for i in combinations(L,2): #i=(4,7)
            dict_items = d.items()
            #first_two = list(dict_items)[i[1]:i[2]] donne les i emes premieres clés et valeurs
            u=i[0] #la premiere clé avec sa valeur u=4
            v=i[1] #la deuxieme clé avec sa valeur v=7
            C=[] #Common neighborhood
            N=[] #Non-Common neighborhood
            for x in d[u] : #boucles qui parcourt les valeurs de la premiere clé,
                if x in d[v]:
                    C.append(x)#si elle les trouve dans les valeurs de la deuxieme clé, elle les ajoutes dans C
                else:
                    N.append(x)#sinon elle les mets dans N
            N2=[]
            for x in d[v] :#parcourt les valeurs de la deuxieme clé
                if x in d[u]:
                    continue
                else:
                    N2.append(x)
            N+=N2
            #N.remove(u)
            #N.remove(v)
            N2=[]
            D=C+N
            count = 0
            for j in D:
                V=d[j]
                L = D
                p = set(D).difference(set(V))  # p=[5,6,3,1,8,7,11]
                for i in V:
                    if i in p:
                        p.remove(i)
                count += len(p)


        #print("C=",C)
        #print("N=",N)
        #print("N2=",N2)
        #print(d.keys)
        #print(d)
        print(count)
        print("Fin du ficheir")
        print('===================================')
        #print(first_two)
