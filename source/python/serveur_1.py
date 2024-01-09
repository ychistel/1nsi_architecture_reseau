import socket

# Paramètres du serveur
host_serveur = '127.0.0.1'
port_serveur = 12345

# création d'un objet socket
serveur_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# liaison du socket avec une adresse et un port
serveur_socket.bind((host_serveur, port_serveur))

# Attente de connexions entrantes (maximum 5 connexions en attente)
serveur_socket.listen(5)

# acceptation d'une connexion entrante
client_socket, client_adresse = serveur_socket.accept()
ip_client, port_client = client_adresse
print(f"Serveur > Connexion avec {ip_client}:{port_client}")

# ------------------------------------------------------------
# Début de l'échange entre le serveur et le client

# reception des données depuis le client
donnees_recues = client_socket.recv(1024)
# affichage des données reçues
print(f"Client > {donnees_recues.decode('utf-8')}")

# envoi d'une réponse du serveur au client
reponse = "OK : message reçu"
client_socket.send(reponse.encode('utf-8'))

# Fin de l'échange entre le serveur et le client
# ------------------------------------------------------------

# fermeture des sockets
client_socket.close()
serveur_socket.close()