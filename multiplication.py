number = int(input("Enter the number: "))
largeList =[]
for i in range(number):
    smallList=[]
    for j in range(i+1):
        smallList.append((j+1)*(i+1))
    largeList.append(smallList)
print(largeList)