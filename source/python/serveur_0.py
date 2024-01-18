# coding=utf8
from socket import *

### Mise en place du service ########
MON_IP='xxx.xxx.xxx.xxx'
PORT = 50000
service = socket(AF_INET, SOCK_STREAM)
try:
    service.bind((MON_IP , PORT))
    tourne = True
except error :
    print("Impossible de démarrer le service.")
    tourne = False

while tourne :
    print("Serveur prêt, en attente de requètes ...")
    service.listen(1)
    ### Mise en place d?une connexion ########
    connexion, adresse = service.accept()
    print("Client connecté. : ",adresse[0])
    ### Dialogue avec le client ########
    message = ""
    while message.upper() != "FIN" :
        message = input("moi > ")
        connexion.send(message.encode("utf8"))
        if message.upper() != "FIN" :
            message = connexion.recv(1024).decode("utf8")
            print("client > ", message)
    connexion.close()

    ch = input("<R>ecommencer <T>erminer ? ")
    ch = ch[0].upper()
    if ch =='T':
        tourne = False

service.close()