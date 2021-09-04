
def main():
    #escribe tu código abajo de esta línea
    index = int(input("Enter the index: "))
    num1=0
    num2=1
    serie=1
    total=0
    
    while index>=serie:
        num1=num2
        num2=total
        total=num1+num2
        serie+=1
    
    print(total)

if __name__=='__main__':
    main()
