
def main():
    #Escribe tu código debajo de esta línea
    height = int(input("Enter triangle height: "))
    espacios = height-1
    ast = 1

    while height<ast:
        break
    while height>=ast:
        print((espacios*" ")+"*"*ast)
        ast+=1
        espacios-=1


if __name__=='__main__':
    main()
