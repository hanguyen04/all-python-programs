studentMarks=["Ron",56], ["Alan",85], ["Christine",68],["David",72]
#lambda helps sorts the right column in a 2D list
#x:x represents the number
sortedSMAscending=sorted(studentMarks, key=lambda x:x[1])
for n in range(len(studentMarks)):
    print(sortedSMAscending[n])
