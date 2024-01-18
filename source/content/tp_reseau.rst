TP : Simuler un réseau
======================

Un réseau local
---------------

Cet exercice simule un réseau avec le logiciel *filius*.

#. Créer un réseau nommé JULES contenant trois PC dont l’adresse réseau est ``192.168.0.0/24``. Les adresses IP des trois
   PC ont leurs derniers octets égaux à 21, 22 et 23.
#. Au réseau JULES, ajouter un serveur d’adresse IP : ``192.168.0.1``. Vérifier que les PC communiquent avec le serveur.
#. Ajouter sur le serveur l’application "Serveur web" et démarrer le service.
#. Ajouter sur la machine A l’application "Navigateur web".

   Lancez le navigateur et saisissez l’adresse IP du serveur web pour afficher la page web.

Résolution de nom de domaine
----------------------------

L’accès à un serveur web par son adresse IP est possible mais en général on utilise une url écrite de façon à pouvoir
la mémoriser facilement. La transformation de l’url en adresse IP se fait avec un serveur DNS.

#. Ajouter un second serveur au réseau nommé "Serveur DNS" dont l’adresse IP est : 192.168.0.2 avec le même masque de réseau.
#. Repasser en mode simulation et ajouter l’application "Serveur DNS" au serveur dédié.
#. Lancez l’application "Serveur DNS" et élargissez la fenêtre pour bien voir les 3 onglets.

#. Dans le premier onglet, ajouter le nom de domaine "www.dumont-nsi.fr," l’adresse IP du serveur web puis cliquer sur
   ajouter. Démarrer le service.

#. Sur la machine A, vérifiez que la page web s’affiche en saisissant ``http://www.dumont-nsi.fr`` .

#. Si vous avez rencontré un problème :

   - vérifiez que le service DNS est bien démarré;
   - que le nom de domaine est correctement écrit;
   - que l’adresse IP du serveur DNS est bien renseigné sur la machine A (et les autres aussi).

#. Affichez la table d’échange de données de la machine A et des deux serveurs. Quel est le protocole utilisé par le
   serveur DNS ?

Routage entre 2 réseaux
-----------------------

#. Créer un second réseau DUMONT composé de 2 portables, un serveur web et un switch selon les paramètres suivants:

   - adresse de réseau : 172.16.1.0
   - masque de sous reseau : 255.255.255.0
   - serveur web : 172.16.0.5

#. Ajouter un routeur pour relier les deux réseaux. Celui-ci aura 2 interfaces réseaux.

   - une interface vers le réseau JULES d’ip 192.168.0.254
   - une interface vers le réseau DUMONT d’ip 172.16.0.254

#. Le ping du portable de Dumont vers la machine A de Jules est-il un succès ? Pourquoi ?

#. Pour communiquer entre 2 réseaux, il faut que le routeur soit identifié en tant que passerelle sur chaque machine du
   réseau.

   Renseigner sur chaque machine des réseaux JULES et DUMONT la passerelle avec les adresses IP du routeur.

#. Vérifier qu’un ping du portable du réseau DUMONT vers une machine du réseau JULES est fonctionnel.

#. Ajouter l’application "Navigateur web" sur le portable est afficher la page web http://www.serveur-nsi.fr. En cas
   d’erreur, vérifier que tout est bien renseigné sur le portable.
