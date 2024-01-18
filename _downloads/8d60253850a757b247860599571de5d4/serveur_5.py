import socket
import threading

# Paramètres du serveur
host = '127.0.0.1'
port = 12345

# Liste pour stocker les connexions clientes
connexions_clients = []


# Création d'un objet socket
serveur_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Liaison du socket avec une adresse et un port
serveur_socket.bind((host, port))

# Attente de connexions entrantes (maximum 5 connexions en attente)
serveur_socket.listen(5)
print(f"Le serveur écoute sur {host}:{port}")

# Gestion des différentes connexions
# ----------------------------------

def gerer_client(client_socket, client_address):
    print(f"Connexion établie avec {client_address}")
    
    try:
        while True:
            # Réception de données depuis le client
            donnees_recues = client_socket.recv(1024)
            valeur = donnees_recues.decode('utf-8')
            print(f"valeur reçue de {client_address}: {valeur}")            
            print(f"client_socket : {client_socket}")
            # Transmettre le message à tous les autres clients
            for autre_client, _ in connexions_clients:
                autre_client.sendall(valeur.encode('utf-8'))

    except Exception as e:
        print(f"Erreur lors de la communication avec {client_address}: {e}")

    finally:
        # Fermeture du socket client
        client_socket.close()
        print(f"Connexion avec {client_address} fermée")

# Echange de données entre les clients
# Un thread permet d'exécuter la fonction gérer-client pour chaque client

try:
    while True:
        # Acceptation d'une connexion entrante
        client_socket, client_address = serveur_socket.accept()
        
        # Ajout de la connexion cliente à la liste
        connexions_clients.append((client_socket, client_address))
        print("connexions_clients :", connexions_clients)
        # Démarrage d'un thread pour gérer la connexion cliente
        thread_client = threading.Thread(target=gerer_client, args=(client_socket, client_address))
        thread_client.start()

except KeyboardInterrupt:
    print("Arrêt du serveur.")
    serveur_socket.close()
