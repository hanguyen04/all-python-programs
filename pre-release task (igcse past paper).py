itemNum = int(input("Please enter the number of items:"))

while itemNum <2: #making sure that the number of items is over 2
    print('There must be at least 2 items.')
    itemNum = int(input("Please enter the number of items:"))

itemID = [None]*itemNum
desc = [None]*itemNum
resvPrice = [None]*itemNum
bidNum = [0]*itemNum
highestBid = [0]*itemNum
highestID = [None]*itemNum
soldOrNot = [None]*itemNum

for i in range (itemNum):#adding itemID, description and reserve price
    print("Please enter the ID of the item",i+1,'',end='')
    userItemInput = input()
    while True:
        if userItemInput in itemID:#if the item is in the array already
            userItemInput = input("The ID is not unique. Please enter the ID again.")
        else: break#if not - break and add the item to the list
    itemID[i] = userItemInput
    desc[i] = input("Please enter the description: ")
    resvPrice[i] = float(input("Please enter the reserve price: "))
    print("\n")

#task2

for i in range(itemNum):#printing out the itemID, description and the current highest bid
    print("Item ID:",itemID[i])
    print("Description:",desc[i])
    print("Current highest bid:",highestBid[i],"\n")


ItemNum = 0
userBid = 0
userID = ''

ItemNum = input('Type "END" to end. Please enter the item ID:')
while ItemNum != "END":
    if ItemNum in itemID:#if itemID matches one of the values in the itemID array
        print("Item number accepted")
        bidIndex = itemID.index(ItemNum) #the index of the item - can be used to assign other values such as highestID and bid for the item.
        userID = input("Please enter your ID")
        while True:
            userBid = float(input('Please enter the amount you would like to bid:'))
            if userBid > highestBid[bidIndex]:
                highestBid[bidIndex] = userBid
                highestID[bidIndex] = userID
                bidNum[bidIndex] +=1
                print('Bid accepted. Thank you.\n')
                break
            else:
                print('The amount is smaller than the current highest bid.')
    else:
        print('Invalid item number')
    ItemNum = input('Type "END" to end. Please enter the item ID:')

#END to be entered by the company at the end of the auction


#task3
totalFee = 0
numSold = 0
noBid = 0
notMet = 0

for i in range (itemNum):
    if highestBid[i] >= resvPrice[i]:
        soldOrNot[i] = "sold" #highestBid higher than the reserve price
        totalFee += (highestBid[i])*0.1 #10% fee from all sold items
print('\n\n -Total fee: $',totalFee, sep='')

print(' -These items have met their reserve price:')
for i in range (itemNum):
    if soldOrNot[i] == "sold": #if marked "sold" from line 62 then printed
        print("itemID:",itemID[i],"highest bid:",highestBid[i])
        numSold += 1
        
print(" -These items have had no bids:")
for i in range (itemNum):
    if highestBid[i] == 0: #this was initally set as 0; which means those left untouched
        print(itemID[i])
        noBid += 1
        
notMet = itemNum - numSold - noBid #(number of Not met = total - sold - no bid)

print("\nThe number of items sold is:",numSold)
print("The number of items with no bids is:",noBid)
print("The number os items that have not met their reserve price is",notMet)
