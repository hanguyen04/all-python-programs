print("Enter name of artist to match with the person who likes it") 
choice=input()
file = open("classmates info 2.0","r")
print (file.readline(choice))
