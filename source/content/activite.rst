Fonctionnement d’un réseau
==========================

Un réseau local
---------------

Lorsque plusieurs machines veulent communiquer entre elles, il est nécessaire de les relier dans un même réseau. On
va réaliser virtuellement un réseau avec le logiciel **Filius**.

#. Créer un réseau avec trois portables A, B et C.

   - les adresses IP des portables A, B et C sont respectivement ``192.168.0.10``, ``192.168.0.11`` et ``192.168.0.12``.
   - le masque de réseau est ``255.255.255.0``.

   .. figure:: ../img/reseau_local_1_ABC.png
      :align: center
      :width: 400
   
#. Expliquer la présence du **switch** dans le réseau local.
#. La commande ``ping IP`` permet de vérifier la communnication entre 2 machines d'un même réseau. 

   a) Ajouter l'application `commande` sur le portable A.
   b) Vérifier qu'il peut communiquer avec les 2 autres portables B et C.

#. Le masque de réseau détermine le nombre de machines qui peuvent se connecter au réseau.

   -  Combien de valeurs différentes y a-t-il entre le masque et la valeur `255.255.255.255` ?
   -  On obtient l'adresse réseau en appliquant un **ET** binaire entre l'adresse IP d'un portable du réseau local et le masque. Quelle est l'adresse du réseau local ?
   -  Quelle est la dernière adresse IP possible pour ce réseau local ? 
   
#. L'adresse réseau ne peut pas être donnée à une machine. L'adresse de diffusion est la dernière IP possible du réseau et ne peut pas être attribuée à une machine. Combien de machines peut-on connecter au réseau local dont le masque est ``255.255.255.0`` ?


Communication entre 2 réseaux
-----------------------------

On s'intéresse à la communication entre 2 réseaux locaux distincts. Au premier réseau local, on ajoute un second réseau dont l'adresse réseau est ``10.0.0.0`` et de masque de réseau ``255.255.255.240``. Ce réseau contient 2 portables D et E.

.. container:: center

   .. image:: ../img/reseau_local_ABC_DE.png
      :alt: image
      :align: center
      :width: 480
      
#. Créer ce second réseau local sur Filius. À quelle plage d'adresses IP doivent appartenir les portables D et E pour être dans le même réseau?
#. Pour relier 2 réseaux locaux distincts, on ajoute un **routeur** entre les 2 réseaux.

   a) Ajouter sur votre réseau un routeur avec 2 interfaces réseaux. Vous devez obtenir un réseau comme le montre la figure ci-dessous:

      .. image:: ../img/reseau_local_2_ABCDE.png
         :alt: image
         :align: center
         :width: 480

   b) Il faut donner une adresse IP à chaque interface du routeur sachant:

      - que l'interface du routeur reliée au LAN 1 est joignable par les machines A,B,C;
      - que l'interface du routeur reliée au LAN 2 est joignable par les machines D,E;

      Quelles sont les adresses IP que l'on peut donner aux 2 interfaces du routeurs ? Ajouter ces adresses IP à votre routeur. 

#. Exécuter la commande ``ping`` entre les portables A et E des 2 réseaux.

   a) Est-ce que la commande a réussi ?
   b) Pour qu'une machine communique avec une machine extérieure à son réseau, il faut ajouter sur la machine l'adresse IP du routeur du réseau en tant que passerelle. Compléter les passerelles de chaque machine et vérifier que les machines communiquent.
   
Communication sur internet
--------------------------

La communication entre 2 machines sur internet consiste en l'échange de données entre les 2 machines. Comment
procèdent-elles ?

Pour le comprendre, nous allons ajouter le programme **client générique** sur le portable A et le programme **serveur générique** sur le portable E.

#. Etablir la connexion en démarrant le serveur générique en cliquant sur le bouton **connecter** du client
   générique.

   a) Faire un clic droit sur le portable A et afficher la table d'échange des données.
      Vérifier que la table d'échange des données affiche une table similaire à la capture suivante:

      .. figure:: ../img/table_echange_donnees_1.png
         :align: center
         :width: 560
         :class: b-8

   b) Sélectionner la seconde ligne de la table. En-dessous, des informations sur la communication sont affichées. On remarque 2 parties "Réseau" et "Internet" correspondant à 2 couches de communication entre les machines.

      - Quelles sont les adresses IP ? De quelles machines s'agit-il ?
      - Quel est le protocole utilisé pour la couche "Internet" ?

   c) Sélectionner dans la table une ligne de la couche "Transport".

      - Deux nombres sont ajoutés pour cette couche. A quoi correspond celui de la source ?
      - Quel est le protocole utilisé par la couche "Transport"

#. Sur le portable A, envoyer le message "Bonjour le monde !" avec le client générique. La table d'échange affiche 4 nouvelles lignes.

   a) Quelles sont les couches de ces 4 nouvelles lignes ?
   b) Quelles sont les principales différences entre ces quatre lignes ?
   c) Selon vous, pour quelle raison le serveur renvoie-t-il le message au client ?
