import socket

# paramètres du client
host = '127.0.0.1'
port = 12345

# création d'un objet socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connexion au serveur
client_socket.connect((host,port))

# envoi de donnees du client au serveur
message = "Hello, serveur !"
client_socket.send(message.encode('utf-8'))
print(f"Client > {message}")

# reception de la reponse du serveur
reponse = client_socket.recv(1024)
print(f"Serveur > {reponse.decode('utf-8')}")

# fermeture du socket : fin de communication
client_socket.close()