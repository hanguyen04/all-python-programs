def detohex(): 
    print("den to hex") 
    a = int(input())
    b = hex(a)
    c = str(b)
    print(c)

def dentobin(): 
    print("den to bin")  
    a = int(input())
    b = bin(a)
    c = str(b)
    print(c)

def bintoden(): 
    print("bin to den") 
    a=input()
    b=int(a, 2)
    print(b)

def bintohex():
    print("bin to hex") 
    a=input()
    b=int(a, 2)
    c=hex(b)
    print(c)

def hextoden():
    print("hex to den") 
    a=input()
    b=int(a, 16)
    print(b)

def hextobin(): 
    print("hex to bin") 
    a=input()
    b=int(a, 16)
    c=bin(b)
    print(c)

#main program
n=1
while n==1:
    go=input("Enter n to end program")
    while go !=n:
        print("What do you want to convert?")
        choice=int(input("1 for denary\n2 for binary\n3 for hexadecimal"))
        if choice==1:
            choice2=int(input("1 for d to hex\n2 for d to binary"))
            if choice2==1:
                dentohex()
            elif choice2==2:
                dentobin()
            else:
                break
        elif choice==2:
            choice2=int(input("1 for b to denary\n2 for b to hex"))
            if choice2==1:
                bintoden()
            elif choice2==2:
                bintohex()
            else:
                break
        elif choice==3:
            choice2=int(input("1 for h to denary\n2 for h to binary"))
            if choice2==1:
                hextoden()
            elif choice2==2:
                hextobin()
            else:
                break
        else:
            break
        end=input("press n to end")
        if end =="n":
            break
    break

   
        
        
        


























