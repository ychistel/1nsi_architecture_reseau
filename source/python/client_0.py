import socket

# paramètres du client
host = '127.0.0.1'
port = 12345

# création d'un objet socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connexion au serveur
client_socket.connect((host,port))

# envoi de donnees au serveur
message = "Hello, serveur !"
client_socket.sendall(message.encode('utf-8'))

# reception de la reponse du serveur
reponse = client_socket.recv(1024)
print(f"Serveur > {reponse.decode('utf-8')}")

# fermeture du socket
client_socket.close()