def dtob():
    num=int(input("Enter the number"))
    binum=[0,0,0,0,0,0,0,0]
    if num-128 >=0:
        binum[0]=(1)
        num=num-128
    if num-64 >=0:
        binum[1]=(1)
        num=num-64
    if num-32 >=0:
        binum[2]=(1)
        num=num-32
    if num-16 >=0:
        binum[3]=(1)
        num=num-16
    if num-8 >=0:
        binum[4]=(1)
        num=num-8
    if num-4 >=0:
        binum[5]=(1)
        num=num-4
    if num-2 >=0:
        binum[6]=(1)
        num=num-2
    if num-1 >=0:
        binum[7]=(1)
        num=num-1
    print(binum)


def btod():
    binum=input("Enter number")
    len(binum)
    num=0
    if binum[0]==("1"):
        num=num+128
    if binum[1]==("1"):
        num=num+64
    if binum[2]==("1"):
        num=num+32
    if binum[3]==("1"):
        num=num+16
    if binum[4]==("1"):
        num=num+8
    if binum[5]==("1"):
        num=num+4
    if binum[6]==("1"):
        num=num+2
    if binum[7]==("1"):
        num=num+1
    print(num)

def dtoh():
    num=int(input("Enter number"))
    count=0
    while num/16 >=1:
        count=count+1
        num=num-16
    if num == 10:
        num=("A")
    if num == 11:
        num=("B")
    if num == 12:
        num=("C")
    if num == 13:
        num=("D")
    if num == 14:
        num=("E")
    if num == 15:
        num=("F")
    print(count,num)

def htod():
    num1=input("Enter first digit")
    if num1==("A"):
        num1=10
    if num1==("B"):
        num1=11
    if num1==("C"):
        num1=12
    if num1==("D"):
        num1=13
    if num1==("E"):
        num1=14
    if num1==("F"):
        num1=15
    else:
        num1=int(num1)
    num1=num1*16
    num2=input("Enter second digit")
    if num2==("A"):
        num2=10
    if num2==("B"):
        num2=11
    if num2==("C"):
        num2=12
    if num2==("D"):
        num2=13
    if num2==("E"):
        num2=14
    if num2==("F"):
        num2=15
    else:
        num2=int(num2)
    total=num1+num2
    print(total)

def btoh():
    binum=input("Enter number")
    len(binum)
    num1=0
    num2=0
    if binum[0]==("1"):
        num1=num1+8
    if binum[1]==("1"):
        num1=num1+4
    if binum[2]==("1"):
        num1=num1+2
    if binum[3]==("1"):
        num1=num1+1
    #conversion
    if num1 == 10:
        num1=("A")
    if num1 == 11:
        num1=("B")
    if num1 == 12:
        num1=("C")
    if num1 == 13:
        num1=("D")
    if num1 == 14:
        num1=("E")
    if num1 == 15:
        num1=("F")
#second number
    if binum[4]==("1"):
        num2=num2+8
    if binum[5]==("1"):
        num2=num2+4
    if binum[6]==("1"):
        num2=num2+2
    if binum[7]==("1"):
        num2=num2+1
    #conversion
    if num2 == 10:
        num2=("A")
    if num2 == 11:
        num2=("B")
    if num2 == 12:
        num2=("C")
    if num2 == 13:
        num2=("D")
    if num2 == 14:
        num2=("E")
    if num2 == 15:
        num2=("F")
    print(num1,num2)

def htob():
    binum=[0,0,0,0]
    binum2=[0,0,0,0]
    num=input("Enter the number")
    len(num)
    if num[0]==("A"):
        num1=10
    if num[0]==("B"):
        num1=11
    if num[0]==("C"):
        num1=12
    if num[0]==("D"):
        num1=13
    if num[0]==("E"):
        num1=14
    if num[0]==("F"):
        num1=15
    else:
        num1=int(num[0])
    if num1-8 >=0:
        binum[0]=(1)
        num=num-8
    if num1-4 >=0:
        binum[1]=(1)
        num1=num1-4
    if num1-2 >=0:
        binum[2]=(1)
        num1=num1-2
    if num1-1 >=0:
        binum[3]=(1)
        num1=num1-1

    if num[1]==("A"):
        num2=10
    if num[1]==("B"):
        num2=11
    if num[1]==("C"):
        num2=12
    if num[1]==("D"):
        num2=13
    if num[1]==("E"):
        num2=14
    if num[1]==("F"):
        num2=15
    else:
        num2=int(num[1])
    
    if num2-8 >=0:
        binum2[0]=(1)
        num2=num2-8
    if num2-4 >=0:
        binum2[1]=(1)
        num2=num2-4
    if num2-2 >=0:
        binum2[2]=(1)
        num2=num2-2
    if num2-1 >=0:
        binum2[3]=(1)
        num2=num2-1
    print(binum,binum2) 

n=1
while n==1:
    go=input("Enter n to end program")
    while go !=n:
        print("What do you want to convert?")
        choice=int(input("1 for denary\n2 for binary\n3 for hexadecimal"))
        if choice==1:
            choice2=int(input("1 for d to hex\n2 for d to binary"))
            if choice2==1:
                dtoh()
            elif choice2==2:
                dtob()
            else:
                break
        elif choice==2:
            choice2=int(input("1 for b to denary\n2 for b to hex"))
            if choice2==1:
                btod()
            elif choice2==2:
                btoh()
            else:
                break
        elif choice==3:
            choice2=int(input("1 for h to denary\n2 for h to binary"))
            if choice2==1:
                htod()
            elif choice2==2:
                htob()
            else:
                break
        else:
            break
        end=input("press n to end")
        if end =="n":
            break
    break
