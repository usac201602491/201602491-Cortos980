N = 491
lista = []

archivo = open('collatz.txt','w')

for o in range(2,N+1):
    num = o

    def esPar(num):
        if num%2>0:
            return False
        else:
            return True

    while num!=1:
        if(esPar(num)):
            lista.append(int(num))
            num=int(num/2)
        else:
            lista.append(int(num))
            num = int(3*num+1)

    if(num==1):
        lista.append(int(num))        
    print(lista)
    archivo.write(str(lista))
    archivo.write(str("\n"))
    archivo.write(str("\n"))
    archivo.write(str("\n"))
    lista.clear()    
archivo.close()

    
