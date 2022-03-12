str = input("Enter the string: ")
newstr = str
vowels = ['a', 'e', 'i', 'o', 'u']
for s in str.lower():
    if s in vowels:
        newstr = newstr.replace(s,"")

print("the string without the vowels: ",newstr)