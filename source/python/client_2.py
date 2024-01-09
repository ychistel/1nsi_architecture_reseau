import socket

# paramètres du serveur
host = '192.168.1.73'
port = 12345
client = 'client 2'

# création d'un objet socket pour le client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connexion au serveur
client_socket.connect((host,port))

# envoi de donnees au serveur
message = "Hello, je suis le " + client + "!"
client_socket.sendall(message.encode('utf-8'))

# reception de la reponse du serveur
reponse = client_socket.recv(1024)
print(f"Réponse du serveur : {reponse.decode('utf-8')}")

# fermeture du socket
#client_socket.close()
