from os import system
from sys import argv
from time import sleep

count = 0

if len(argv)>=1:
    wordfile = open(argv[1],"r")
    index = 0
    #position = 0
    wordlists = {}
    for each in wordfile:
        wordlists[index] = [each]
        index += 1
        #position = position+len(each)
    pipe = argv[2]
    try:
        sessfile = argv[3]
    except:
        sessfile = "-"
else:
    print('Password Cracker from Online Wordlists using internet connection\npython online_wordlist.py \n arguments:\n\n<wordlist_url_filename>\n"<next pipe command to use these wordlist>\n<session-file to resume wordlist>"\n\n')

if sessfile !="-":
    try:
        sess = open(sessfile,"r")
        count = int(sess.readline())
        print("\n=========SESSION RESUME========\n")
    except:
        count = 0

for i in range(count,index):
    print("\n\n USING WORDLIST " + str(i) + "\n" + str(wordlists[i][0]) ,end="\n\n")
    sleep(2)
    system("curl " + str(wordlists[i][0]).replace("\n","") + "| " + pipe )
    if sessfile !="-":
        sess = open(sessfile,"w")
        sess.write(str(i+1))
        sess.close()
    #system("clear")
    print("COMPLETED WORDLIST " + str(i),end="\n\n")
    sleep(4)
    #system("clear")
print("\n\nWORDLIST COMPLETED SUCCESSFULLY!!!\n\n")
