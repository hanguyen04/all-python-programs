grade=int(input("Please enter your grade as a percentage "))
if grade <= 50 :
    print("U\nCUZ U FAIL HAHAHAHA")
elif grade <= 65 and grade > 50:
    print("D\nsorry bro, there goes your career")
elif grade <= 75 and grade > 65:
    print("C\naverage.\nLike you")
elif grade <= 85 and grade > 75:
    print("B\ngood enough")
elif grade <= 100 and grade >85:
    print("A\ncongrats I guess")
else:
    print("percentage bro, but I'll assume you get U for maths") 
