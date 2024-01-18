# coding=utf8
from socket import *

SERVEUR = 'xxx.xxx.xxx.xxx'
PORT = 50000
liaison = socket(AF_INET, SOCK_STREAM)

try:
    liaison.connect((SERVEUR, PORT))
    message=""
except error:
    print("La connexion a échoué.")
    message="FIN"

# serveur et service
while message.upper() != "FIN" :
    message = liaison.recv(1024).decode("utf8")
    print("serveur >", message)
    if message.upper() != "FIN" :
        message = input("moi > ")
        liaison.send(message.encode("utf8"))

print("Connexion terminée." )
liaison.close()