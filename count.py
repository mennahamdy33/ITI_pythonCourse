
Str = input("write whatever you want  ")
vowels = ['a','e','i','o','u']
countOfVowels=0
for i in Str.lower():
    for v in vowels:
        if(i == v):
            countOfVowels+=1
print("the number of vowels in this string is ",countOfVowels)