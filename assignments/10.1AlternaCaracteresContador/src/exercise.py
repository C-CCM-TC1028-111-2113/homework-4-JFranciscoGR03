def main():
    #escribe tu código abajo de esta línea
    val=int(input())
    cont=val//2
    if val!=0:
        for i in range(cont):
            print("#")
            for i in range(1):
                print("%")

    if val%2!=0:
        print("#")


if __name__=='__main__':   
    main()
