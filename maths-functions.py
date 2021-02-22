import math

def CuboidSA():
    w=float(input("Enter the width: "))
    l=float(input("Enter the length: "))
    d=float(input("Enter the depth: "))
    CuSA=(2*w*l)+(2*w*d)+(2*l*d)
    print(CuSA)

def CuboidV():
    w=float(input("Enter the width: "))
    l=float(input("Enter the length: "))
    d=float(input("Enter the depth: "))
    CuV=w*l*d
    print(CuV)

def TriPriSA():
    b=float(input("Enter the base: "))
    d=float(input("Enter the depth: "))
    h=float(input("Enter the height: "))
    y=b/2
    s=math.sqrt((y**2)+(h**2))
    TPSA=(b*h)+(2*d*s)+(d*b)
    print(TPSA)

def TriPriV():
    b=float(input("Enter the base: "))
    l=float(input("Enter the length: "))
    h=float(input("Enter the height: "))
    TPV=1/2*b*h*l
    print(TPV)

def CylinderSA():
    r=float(input("Enter the radius"))
    h=float(input("Enter the height"))
    CySA=((2*3.14*r**2)+(2*3.14*r))
    print(CySA)

def CylinderV():
    r=float(input("Enter the radius"))
    h=float(input("Enter the height"))
    CyV=((2*3.24*r**2)*h)
    print(CyV)

meh=0
while meh == 0:
    program=input("Press n to end program and space to continue")
    if program =="n":
        break
    else:
        choice=int(input("Enter\n1 to calculate the surface area\n2 to calculate the volume"))
        if choice ==1:
            shape=input("Enter\nCu for cuboid\nTP for Triangular Prism\nCy for Cylinder")
            if shape == "Cu":
                CuboidSA()
            elif shape == "TP":
                TriPriSA()
            elif shape == "Cy":
                CylinderSA()
            else:
                print("invalid input")
        elif choice ==2:
            shape=input("Enter\nCu2 for cuboid\nTP2 for Triangular Prism\nCy2 for Cylinder")
            if shape == "Cu2":
                CuboidV()
            elif shape == "TP2":
                TriPriV()
            elif shape == "Cy2":
                CylinderV()
            else:
                print("invalid input")
        else:
            ("invalid input")
            
        
        
        







    
    
    
                
    
