months=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
rainfall=[0,0,0,0,0,0,0,0,0,0,0,0,0,]
annualRainfall=0
for i in range (0,12):
    print("Please input rainfall for month",months[i])
    rainfall[i]=int(input())
    annualRainfall+=rainfall[i]
averageRainfall=annualRainfall/12
roundedAverage=round(averageRainfall,1)
monthsAboveAverage=0
for i in range (0,12):
    if rainfall[i]>averageRainfall:
        monthsAboveAverage+=1
    print(months[i],rainfall[i])
print("annual rainfall=:",annualRainfall)
print("average monthly rainfall =:", roundedAverage)
print("\nNumber of months above average rainfall:", monthsAboveAverage)

        
