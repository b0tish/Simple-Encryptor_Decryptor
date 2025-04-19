from django.shortcuts import render

import random

def index(request):
    return render(request, "index.html")

def encrypt(request):
    if request.method == "POST":
        message = request.POST.get("text")
        tempkey = request.POST.get("key")


        key=1
        for loop2 in tempkey:
            key=ord(loop2)+key
        for digit in str(key):
            key+=int(digit)



        char_num=40
        LETTERS_chooser=open("letter.txt","r").readlines()
        LETTERS_rng=random.randint(0,9)

        LETTERS_choose=(LETTERS_chooser[int(LETTERS_rng)])
        LETTERS=LETTERS_choose


        for chooser in range(LETTERS_rng):
           char_num+=1
        char_letter=(chr(char_num))


        random_encry=random.randint(1,3)

        letter_for_encry = 33 + random_encry



        encrypted =str()
        for chars in str(message):
            if chars in LETTERS:
                num = LETTERS.find(chars)
                num =(num+key)%95
                #while (num>95):
                    #num = num-95
                encrypted +=  LETTERS[num:num+random_encry]
        encrypted= encrypted + chr(letter_for_encry) + char_letter

        context = {"encrypted" : encrypted, "message":message,"key":tempkey }
        return render(request,"index.html",context)


def decrypt(request):
    if request.method == "POST":
        message = request.POST.get("entext")
        tempkey = request.POST.get("enkey")



        key=1
        for loop2 in tempkey:
            key=ord(loop2)+key

        for digit in str(key):
            key+=int(digit)
        decrypted =str()

        n=0
        m=1
        user_list=[]
        words=[]
        random_var=0
        main_var=0

        char=message[-1]
        LETTERS_choosing=ord(char)-40
        message=message.strip(message[len(message)- 1])

        #for random_var
        char_random_encry = message[-1]
        random_var = ord(char_random_encry) - 33
        message=message.strip(message[len(message)- 1])


        LETTERS_chooser=open("letter.txt","r").readlines()
        LETTERS_choose=(LETTERS_chooser[int(LETTERS_choosing)])
        LETTERS=LETTERS_choose

        i=random_var-1
        main_var = random_var-1
        for chars in str(message):
            if main_var == i:
                if chars in LETTERS:
                    num = LETTERS.find(chars)
                    num =(num-key)%95
                    decrypted +=  LETTERS[num]
                    i=0
            else:
                i=i+1
    context = {"decrypted" : decrypted, "enmessage":message,"enkey":tempkey }
    return render(request,"index.html",context)
