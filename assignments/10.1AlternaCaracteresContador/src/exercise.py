def main():
    #escribe tu código abajo de esta línea
    val=int(input("Ingresa un numero"))
    cont=val//2
    lista=1

    for x,y in enumerate(str(lista)):
        if val!=0:
            for i in range(cont):
                print(str(lista) + "-#")
                lista+=1
                for i in range(1):
                    print(str(lista) + "-%")
                    lista+=1

        if val%2!=0:
            print(str(lista) + "-#")
            lista+=1


if __name__=='__main__':   
    main()
