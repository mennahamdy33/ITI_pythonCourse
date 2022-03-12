def numbers():
    count=0
    sum=0
    while True:
        inp = input("please enter a number, to end type done: ")
        if inp == "done":
            break
        if inp.isdigit():
            sum+=int(inp)
            count+=1
        else:
            print("========== Please enter numbers only===========")
    print(f"you entered {count} numbers,their sum is {sum}, and thier average is {sum/count}")

numbers()