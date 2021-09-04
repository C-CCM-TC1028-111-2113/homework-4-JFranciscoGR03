def main():
    #escribe tu código abajo de esta línea
    val = int(input())
    cont=0
    while cont<val:
        cont+=1
        if cont%2!=0:
            print(str(cont)+"-#")
        else:
            print(str(cont)+"-%")

if __name__=='__main__':   
    main()
