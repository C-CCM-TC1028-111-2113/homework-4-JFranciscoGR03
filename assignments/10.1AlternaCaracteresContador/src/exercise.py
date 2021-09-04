def main():
    #escribe tu código abajo de esta línea
    val = int(input("ingresa un numero"))
    cont=0
    #for cont in range(1,val+1):
    while cont<val:
        cont+=1
        if cont%2!=0:
            print(str(cont)+"-#")
        else:
            print(str(cont)+"-%")

if __name__=='__main__':   
    main()
