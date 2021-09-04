def main():
    #escribe tu código abajo de esta línea
    val = int(input())
    lista=1
    cont=val//2

    while lista<val:
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
