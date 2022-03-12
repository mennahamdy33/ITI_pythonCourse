number = int(input("Enter the number: "))
spaces = 2 * number - 2
for i in range(number):
    for j in range(spaces):
        print(end=" ")
    spaces = spaces - 2
    for j in range(0, i + 1):
        print("* ",end="")
    print("\r")