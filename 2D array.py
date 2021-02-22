mnd = [[None]*5,[None]*5]

mnd1=mnd[0]
for i in range (5):
    name = input("Enter the name of a DVD: ")
    mnd1[i] = name

mnd2=mnd[1]
for i in range (5):
    Dname = input("Enter the name of a director: ")
    mnd2[i] = Dname
        
print(mnd)

chosenTitle=input("Enter the film you want to see: ")
    
print("The film you want to see is:",chosenTitle)
print("The director of the movie is:",mnd2[mnd1.index(chosenTitle)])


