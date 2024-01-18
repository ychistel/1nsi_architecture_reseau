TP : Créer un réseau en Python
=========================

La connexion réseau suit le modèle **client - serveur** dont le principe est :

-   Un serveur écoute les connexions entrantes, il est en attente d'une connexion émise par un client;
-   Un client se connecte au serveur et envoie des données;
-   Le serveur reçoit les données et envoie une réponse;
-   En fin de communication, la connexion est close.

Client et serveur sur la même machine
-------------------------------------

On donne ci-dessous les 2 fichiers python ``serveur.py`` et ``client.py`` qui sont à télécharger sur votre machine.

.. note::

    -   Le fichier python du serveur :download:`serveur.py <../python/serveur.py>`
    -   Le fichier python du client :download:`client.py <../python/client.py>`

#.  Ouvrir l'application Thonny puis ouvrir les 2 fichiers téléchargés.
#.  Quelle est l'adresse IP du serveur ? du client ? A quoi correspond-elle ?
#.  Placez-vous dans le fichier ``serveur``, puis exécutez ce programme en tapant sur les touches CTRL + T.
#.  Placez-vous sur le fichier ``client``, puis exécutez le programme en tapant sur CTRL + T.
#.  Quel est l'échange de données entre le client et le serveur ? Quels sont les ports utilisés par chaque machine ?

Client et Serveur sur 2 machines différentes
--------------------------------------------

La connexion précédente s'est faite sur la même machine, ce qui est rarement le cas dans une communication réseau. Ici, l'objectif est de vous connecter au serveur placé sur la machine de votre voisin.

#.  Ouvrir une fenêtre de commande sur votre machine et saisir la commande ``ipconfig``. Relever l'adresse IP de votre machine et la communiquer à votre voisin.
#.  Modifier le fichier ``client`` en modifiant l'adresse IP du serveur à connecter.
#.  Assurez-vous que le serveur est démarré puis exécutez votre client. Vérifiez que la communication est fonctionnelle entre le client et le serveur.
#.  On va modifier les données à envoyer au serveur. Sur votre client, remplacer l'instruction :

    .. code::

        message = "Hello, serveur !"
    
    par l'instruction de saisie :

    .. code::

        message = input("saisir votre message")

    Exécutez le client et vérifiez que le message saisi est reçu par le serveur.

#.  Maintenant on met en place une communication ping-pong entre le client et le serveur. Le client envoie un message et le serveur répond avec le même message.

    On commence par modifier le fichier ``client.py``

    a)  Créer une variable booléenne ``connexion`` qui a pour valeur ``True`` juste après la variable ``port_serveur``.
    b)  Placer le code d'échange de données dans une boucle ``while connexion`` comme le montre la figure ci-dessous.
    
        .. figure:: ../img/boucle_while_client.png
            :align: center
            :width: 520

    c)  Ajouter dans la boucle ``while`` un test sur le message qui met fin à la communication. Par exemple, si le message envoyé par le client est le mot "fin", la connexion s'arrête.

    d)  Faire de même avec le fichier ``serveur`` en insérant la boucle ``while`` comme sur la figure suivante:

        .. figure:: ../img/boucle_while_serveur.png
            :align: center
            :width: 520


Deux clients et un serveur
--------------------------

Pour faire communiquer 2 clients, on peut utiliser le modèle client-serveur.

.. figure:: ../img/client_serveur.svg
    :align: center
    :width: 520

-   Un serveur est démarré sur une machine;
-   Les 2 clients se connectent au serveur;
-   Les clients communiquent en envoyant les messages au serveur qui se charge de les renvoyer aux autres clients.

.. note::

    Le programme ``serveur`` est donné et n'a pas besoin d'être modifié. Il peut être téléchargé: :download:`serveur <../python/serveur_5.py>`.

    Le programme client de la partie précédente peut être repris sans changement.

#.  Installer le programme ``serveur`` sur une machine et démarrer le.
#.  Installer un premier client sur la même machine que le serveur et installer un second client sur une seconde machine.
#.  Exécuter les programmes clients et contrôler qu'ils sont bien connectés au serveur.
#.  Échanger des messages entre les deux clients et vérifier que les messages passent par le serveur.