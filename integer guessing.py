endloop=0
max=100
min=1
print("think of an interger between 1 and 100")
print("type in enter when ready")
input()
guesses=0

while endloop==0:
    midpoint=int((max+min)/2)
    print("my guess is,",midpoint,"please enter TH, TL, correct")
    rep=input()
    rep=rep.lower
    guesses+=1
    if rep=="th":
        max=midpoint-1
    elif rep=="tl":
        min=midpoint+1
    elif rep=="c":
        endloop==1
        print("your number is",rep) 
        print("It took me",guesses,"guesses to reach the correct answer")
    else:
        print("your reply isn't recognised")
        guesses-=1 
    if guesses>7:
        print("I think you've made a mistake")
