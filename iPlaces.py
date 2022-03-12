Str = input("Enter the string: ")
iPlaces = []
location =0
for i in Str.lower():
    if(i == 'i' ):
        iPlaces.append(location)
    location+=1
for place in iPlaces:
    print("i appeared in location: ",place)