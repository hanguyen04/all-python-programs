file = open("classmates info","w")
classmates=[None]*x
foods=[None]*x
artists=[None]*x
x=int(input("Enter the number of people"))

for i in range(x):
    name = input("Enter name: ")
    classmates[i]=name
    
for i in range(x):
    print("What's",classmates[i],"favorite food: ")
    food=input()
    foods[i]=food
    
for i in range(x):
    print("Who's",classmates[i],"favorite artisist: ")
    artist=input()
    artists[i]=artist
    
for i in range(x): 
    file.write(classmates[i]+","+foods[i]+","+artists[i]+"\n")
file.close()
