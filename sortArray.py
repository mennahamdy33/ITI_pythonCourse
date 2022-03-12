elements = []
for i in range(5):
    elements.append(input("please enter a new element: "))
# elementsAscending = elements.sort()
# elementsDescending = elements.sort(reverse=True)
print("-------------------------------")
print("The elements in an ascending order : ")
elements.sort()
for a in elements:
    print(a)
print("-------------------------------")
print("The elements in an descending order : ")
elements.reverse()
for d in elements:
    print(d)
