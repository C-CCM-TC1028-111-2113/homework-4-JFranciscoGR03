

def main():
    #Escribe tu código debajo de esta línea
    num = int(input("Escribe un numero : "))
    var=1

    while True:
        if (var**2)>num:
            print(var)
            break
        else:
            var+=1

if __name__=='__main__':
    main()
