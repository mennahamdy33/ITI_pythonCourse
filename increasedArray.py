def incArrayfn(length,start):
    incArray=[]
    for i in range(length):
        incArray.append(start)
        start+=1
    return incArray
print(incArrayfn(5,3))