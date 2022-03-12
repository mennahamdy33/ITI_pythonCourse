import webbrowser
import random
websites =['https://www.youtube.com/','https://www.csestack.org/','https://www.geeksforgeeks.org/','https://twitter.com/home','https://www.facebook.com/']
n = random.randint(0,len(websites)-1)
#Open url in default browser
webbrowser.open(websites[n], new=2)