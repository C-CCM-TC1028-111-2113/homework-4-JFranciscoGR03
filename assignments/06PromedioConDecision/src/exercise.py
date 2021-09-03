def main():
    #escribe tu código abajo de esta línea
    num=0
    total=0
    cantidad=0

    while num>=0:
        num=float(input())
        total=total+num
        cantidad+=1
    else:
        total= (total-num)/(cantidad-1)

    print(total)



if __name__=='__main__':
    main()
