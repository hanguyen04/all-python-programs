#TASK 1 
#Declering all the arrays needed (doesn't change)
Processor = ["p3","p5","p7"]
ProcessorPrice=[100,120,200] 
RAM = ["16GB","32GB"]
RAMPrice =[25, 150]
Storage = ["1 TB","2 TB"]
StoragePrice=[50, 100]
Screen = ["19","23"]
ScreenPrice= [65, 120]
Case = ["Mini Tower","MiDi Tower"]
CasePrice= [40 ,70]
USBport = ["2 ports", "4 ports"]
USBPrice = [10, 20] 

#Enter the date & while loop the run for the whole day
date = input("Enter today's date:")
n=0
OrdersMade=0 
customers = [] #array - add variables in later
orderprices = []

while True:
  #array for stocks & number of items sold (TASK 2)
  #these arrays are part of the while loop because it change
  PStock=[12,0, 32] 
  RStock=[25, 0]
  StStock=[22,17]
  ScStock=[1,43]
  CStock=[0,13]
  UStock=[20, 11]

  PSold=[0,0,0]
  RSold=[0,0]
  StSold=[0,0]
  ScSold=[0,0]
  CSold=[0,0]
  USold=[0,0]

  #priting everything for the customer to choose from 
  print("The Processors are", Processor)
  print("The RAMs are", RAM)
  print("The Storages are", Storage)
  print("The Cases are", Case)
  print("The USBports are", USBport)

  #choosing the things needed 
  print ("Please enter the number of position of the chosen component in the array (start from 0)") 
  choiceP = int(input("Enter the processor position")) #number in position to search in array 
  choiceR = int(input("Enter the RAM position"))
  choiceSt = int(input("Enter the Storage position"))
  choiceSc = int(input("Enter the Screen position"))
  choiceC = int(input("Enter the Case position"))
  choiceU = int(input("Enter the USB ports position"))
  
  #finding the chosen component 
  ProcessorChosen = Processor[choiceP]
  RAMChosen = RAM[choiceR]
  StorageChosen = Storage[choiceSt]
  ScreenChosen = Screen[choiceSc]
  CaseChosen = Case[choiceC]
  USBportChosen = USBport[choiceU]
  
  #finding the price for each component 
  PChosenPrice = ProcessorPrice[choiceP]
  RChosenPrice = RAMPrice[choiceR]
  StChosenPrice = StoragePrice[choiceSt]
  ScChosenPrice = ScreenPrice[choiceSc]
  CChosenPrice = CasePrice[choiceC]
  UChosenPrice = USBPrice[choiceU]

  #calculating the total cost for everything (task1)
  totalCost = (PChosenPrice + RChosenPrice + StChosenPrice + ScChosenPrice + CChosenPrice + UChosenPrice)*1.2
  print("The estimated price is $",totalCost)


  #TASK 2
  #searching for the stocks of each item 
  PStockChosen = PStock[choiceP]
  RStockChosen = RStock[choiceR]
  StStockChosen = StStock[choiceSt]
  ScStockChosen = ScStock[choiceSc]
  CStockChosen = CStock[choiceC]
  UStockChosen = UStock[choiceU]

  #changing the stocks and calculating the number sold 
  while PStockChosen == 0:
   print("The processor chosen is out of stock") 
   choiceP = int(input("Enter the processor position"))
   ProcessorChosen = Processor[choiceP] #enter & find another version 
   PChosenPrice = ProcessorPrice[choiceP]
   PStockChosen = PStock[choiceP]
  PStock[choiceP] -=1 #update stocks 
  PSold[choiceP] +=1 #to be printed later 

  while RStockChosen == 0:
   print("The processor chosen is out of stock")
   choiceR = int(input("Enter the RAM position"))
   RAMChosen = RAM[choiceR]
   RChosenPrice = RAMPrice[choiceR]
   RStockChosen = RStock[choiceR]
  RStock[choiceR] -=1
  RSold[choiceR] +=1

  while StStockChosen == 0:
   print("The storage chosen is out of stock")
   choiceSt = int(input("Enter the storage position"))
   StChosen = Storage[choiceSt]
   StChosenPrice = StoragePrice[choiceSt]
   StStockChosen = StStock[choiceSt]
  StStock[choiceSt] -=1
  StSold[choiceSt] +=1

  while ScStockChosen == 0:
   print("The screen chosen is out of stock")
   choiceSc = int(input("Enter the Screen position"))
   ScChosen = Screen[choiceSc]
   ScChosenPrice = ScreenPrice[choiceSc]
   ScStockChosen = ScStock[choiceSc]
  ScStock[choiceSc] -=1
  ScSold[choiceSc] +=1

  while CStockChosen == 0:
   print("The case chosen is out of stock")
   choiceC = int(input("Enter the Case position"))
   CChosen = Case[choiceC]
   CChosenPrice = CasePrice[choiceC]
   CStockChosen = CStock[choiceC]
  CStock[choiceC] -=1
  CSold[choiceC] +=1

  while UStockChosen == 0:
   print("The USB por chosen is out of stock")
   choiceU = int(input("Enter the USB ports position"))
   UChosen = USBport[choiceU]
   UChosenPrice = USBPrice[choiceU]
   UStockChosen = UStock[choiceU]
  UStock[choiceU] -=1
  USold[choiceU] +=1
  
  #Order information 
  customer = str(input("enter the customer's name: ")) 
  customers.append(customer) #append use to add the information into the array 
  orderprice = totalCost
  orderprices.append(orderprice)

 #print out everything that customer bought
  for i in range [2]: #print twice for customer & store
    print ("The components chosen for",customers[n], "are", ProcessorChosen,",",RAMChosen,",", StorageChosen,",", ScreenChosen,",", CaseChosen,",", USBportChosen)
  OrdersMade =+1 #calculate the numbers of orders made 
  print("has the day ended yet? Enter yes to end and press enter to continue")
  Ended=str(input()) 
  if Ended == "yes":
    break #break to exit the loop as the day had ended
  else: #loop over the chunk of code to make another order 
    n=+1 

#TASK 3: Printng out everything which needs to be printed 
print("There were",OrdersMade,"orders made") 
print("Today's date:",date)
print(customers)
print(orderprices)
print ("The number of processors sold are", PSold) 
print ("The number of RAM sold are", RSold)
print ("The number of Storage sold are",StSold )
print ("The number of Screen sold are", ScSold)
print ("The number of Case sold are", CSold)
print ("The number of USB ports sold are",USold )
