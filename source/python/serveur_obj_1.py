import socket

class Serveur:
    
    def __init__(self,host='127.0.0.1',port=12345):
        # Paramètres du serveur
        self.ip_serveur = host
        self.port_serveur = port
        self.serveur_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # liaison du socket avec une adresse et un port
        self.serveur_socket.bind((self.ip_serveur, self.port_serveur))

        # Attente de connexions entrantes (maximum 5 connexions en attente)
        self.serveur_socket.listen(5)

        # acceptation d'une connexion entrante
        self.client_socket, self.client_adresse = self.serveur_socket.accept()
        ip_client, port_client = self.client_adresse
        print(f"Serveur > Connexion avec {ip_client}:{port_client}")

Serveur()
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