import re
num=1
while num != 0:
    code = input("Enter your postcode: ")
    valid = re.match("[A-Z]+[0-9]+\s[0-9][A-Z][A-Z]",code)
    #1/2 letters/number space 1 number & 2 letters
    while not valid:
        print("Erm, try again!")
        code = input("Enter your postcode: ")
        valid = re.match("[A-Z]+[0-9]+\s[0-9][A-Z][A-Z]",code)
    print("That looks OK")
    #end program
    num=int(input("Enter 0 to end program and 1 to continue"))
    if num ==0:
        break
   
    

