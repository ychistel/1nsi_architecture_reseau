import socket

# Démarrage de la connexion serveur
# ---------------------------------

# Paramètres du serveur
ip_serveur = '192.168.1.73'
port_serveur = 12345

# création d'un objet socket
serveur_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# liaison du socket avec une adresse et un port
serveur_socket.bind((ip_serveur, port_serveur))

# Attente de connexions entrantes (maximum 5 connexions en attente)
serveur_socket.listen(5)

# Affichage de la connexion avec un client
print("Serveur démarré. En attente de connexion !")
print("--"*30)


# Attente de connexion client
# ---------------------------

# acceptation d'une connexion entrante
client_socket, client_adresse = serveur_socket.accept()

# adresse IP et port utilisé par le client
ip_client, port_client = client_adresse

# affichage d'une connexion client
print(f"Connexion avec client d'adresse IP: {ip_client}:{port_client}")


# Echange de données entre client et serveur
# ------------------------------------------

# reception des données depuis le client
donnees = client_socket.recv(1024)

# affichage des données reçues
print(f"Client a écrit : {donnees.decode('utf-8')}")

# envoi d'une réponse du serveur au client
reponse = f"OK, message reçu depuis l'adresse {ip_client}:{port_client}"
client_socket.send(reponse.encode('utf-8'))


# Fin de connexion entre le serveur et le client
# ----------------------------------------------

print("fermeture de la connexion")
# fermeture des sockets
client_socket.close()
serveur_socket.close()