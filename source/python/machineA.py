import socket



donnee = b'Hello world'
#emetteur.sendto(donnee,('localhost',56789))

def envoiAvecBit(donnee,bit,emetteur,adresse,port):
    x =bytearray(donnee) # transforme la donnée (chaîne) en tableau d'octets
    x.append(bit) # ajoute le bit de contrôle
    emetteur.sendto(x, (adresse,port))


emetteur = socket.socket(type=socket.SOCK_DGRAM)


envoiAvecBit(donnee,1,emetteur,'localhost',56789)