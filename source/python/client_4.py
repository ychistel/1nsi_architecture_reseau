import socket

# paramètres du client
host = '127.0.0.1'
port = 12345
connexion = True

# création d'un objet socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connexion au serveur
client_socket.connect((host,port))

while connexion:
    # Invite de commande pour saisir un message : Client > ...
    message = input("Client > ")
    
    # envoi de donnees au serveur
    client_socket.sendall(message.encode('utf-8'))

    # reception de la reponse du serveur
    reponse = client_socket.recv(1024)
    # affichage de la reponse du serveur au client
    print(f"Serveur > {reponse.decode('utf-8')}")

    # arrêt de la communication si le message est FIN ou fin
    if message.upper() == 'FIN':
        connexion = False
        
# fermeture du socket
client_socket.close()