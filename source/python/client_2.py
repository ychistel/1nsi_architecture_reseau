import socket

# Connexion du client au serveur
# ------------------------------

# paramètres du serveur
ip_serveur = '192.168.1.73'
port_serveur = 12345

# création d'un objet socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connexion au serveur
client_socket.connect((ip_serveur,port_serveur))

# adresse IP et port utilisé par le client
ip_client,port_client = client_socket.getsockname()

# Affichage de la connexion
print("Le client est connecté")
print(f"Le serveur a pour adresse {ip_serveur} qui utilise le port {port_serveur}")
print(f"le client utilise l'adresse {ip_client} et le port {port_client}")
print("--"*30)


# Envoi de donnees du client au serveur
# -------------------------------------
message = input("Saisir votre message : ")
print(f"Client envoie : {message}")
client_socket.send(message.encode('utf-8'))


# reception de la reponse du serveur
# ----------------------------------
reponse = client_socket.recv(1024)
print(f"Serveur répond : {reponse.decode('utf-8')} ")


# fermeture du socket : fin de communication
# ------------------------------------------
client_socket.close()