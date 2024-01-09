import socket

# Paramètres du serveur
host = '127.0.0.1'
port = 12345

# création d'un objet socket
serveur_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# liaison du socket avec une adresse et un port
serveur_socket.bind((host, port))

# Attente de connexions entrantes (maximum 5 connexions en attente)
serveur_socket.listen(5)

# acceptation d'une connexion entrante
client_socket, client_adress = serveur_socket.accept()
print(f"Connexion établie avec {client_adress}")

# reception des données depuis le client
donnees_recues = client_socket.recv(1024)
print(f"données reçues du client : {donnees_recues.decode('utf-8')}")

#  envoi d'une réponse au client
reponse = "message reçu !"
client_socket.sendall(reponse.encode('utf-8'))

# fermeture des sockets
client_socket.close()
serveur_socket.close()