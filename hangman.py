import random
def askname():
    name = input("\033[1mplz enter your name \033[0m")
    if name.isalpha():
        return name
    print("\033[93m======== please enter your first name with alphabets only====== \033[0m")
    return askname()
def validation():
    trial = input("\033[1mplease enter an alphabet: \033[0m")
    if trial.isalpha() and len(trial)==1:
        return trial
    print("\033[93m======== please enter one alphabet====== \033[0m")
    return validation()
def hangman():
    global listOfWords
    randNum = random.randint(0, len(listOfWords))
    currentWord = listOfWords[randNum]
    trialWord=[str("")]*len(currentWord)
    name = askname()
    print(f"\033[95m==== Hello {name}====\033[0m")
    print(f"\033[95m==== Welcome to hangman game ====\033[0m")
    print(f"\033[1mthe word should be {trialWord}\033[0m")
    rightAnswers=0
    for i in range(7):
        trial = validation()
        lst=[]
        for pos, char in enumerate(currentWord):
            if (char == trial) and char not in trialWord :
                lst.append(pos)
        if len(lst)==0:
            print("\033[91mwrong! guess again\033[0m")
        else:
            rightAnswers += len(lst)
            for index in lst:
                trialWord[index] = trial
            if (rightAnswers == len(currentWord)):
                result = ""
                print(f"\033[92mGreat you got it right the word is {result.join(trialWord)}\033[0m")
                break
            else:
                print("\033[94mAwesome, continue the great work  \033[0m")
        print( f"\033[1mthe word should be {trialWord}\033[0m")

    else:
        print( f"\033[91myou lost! good luck next time\033[0m")
listOfWords=["pen","user","tea","shirt","font","two","mouse","pop"]
hangman()