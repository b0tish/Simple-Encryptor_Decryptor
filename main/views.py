from django.shortcuts import render

from .utils.crypto import encrypt_message, decrypt_message


def index(request):
    return render(request, "index.html")


def encrypt(request):
    if request.method == "POST":
        message = request.POST.get("text")
        tempkey = request.POST.get("key")
        encrypted = encrypt_message(message, tempkey)
        context = {"encrypted": encrypted, "message": message, "key": tempkey}
        return render(request, "index.html", context)
    else:
        return render(request, "index.html")


def decrypt(request):
    if request.method == "POST":
        message = request.POST.get("entext")
        tempkey = request.POST.get("enkey")
        decrypted = decrypt_message(message, tempkey)
        context = {"decrypted": decrypted, "enmessage": message, "enkey": tempkey}
        return render(request, "index.html", context)
    else:
        return render(request, "index.html")
