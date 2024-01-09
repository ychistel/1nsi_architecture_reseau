import socket


def recoitAvecBit(receveur):
    """ Attend la réception d'un message et retourne (donnee, bit, adresse) """
    message, adresse =receveur.recvfrom(1500)
    bit, donnee =decoderPaquet(message)
    return(donnee, bit, adresse)
                                                                                                                                                                                        
# Fonction à fournir aux élèves
def decoderPaquet(donnee):
    """ Extrait de `donnee` le bit de contrôle et le contenu du message """
    # on utilise une facilité de Python appelée "tranches" (slices)
    # pour "découper" le message en bit de contrôle (dernier octet : donnee[-1])
    # et reste du message (donnee[:1] = tout le tableau sans le dernier octet)
    return(donnee[-1], donnee[:-1])

receveur = socket.socket(type=socket.SOCK_DGRAM)
receveur.bind(('localhost',56789))


donnees, bit, adresse = recoitAvecBit(receveur)

print(donnees,bit,adresse)