



#lista=[2, 6, 8, 2, -66, 34, -35, 66, 700, 1002, -84, 10, 4]

def find_outlier(integers):
    cont=0
    contimp=0
    for i in integers:
        i=abs(i)
        if i%2==0:
            l=i
            cont=cont+1
        else:
            k=i
            contimp=contimp+1

    if contimp<cont:
        return k 
    else:
        return l


#print(find_outlier(lista))




