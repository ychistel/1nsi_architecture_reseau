Exercices
=========

Exercice 1
----------

Dans un réseau local, une machine a pour adresse IPv4 ``10.127.0.15/24``.

#. Donner la notation binaire de l'adresse IP de cette machine.
#. Quel est le masque réseau de cette machine en notation décimale puis en binaire.
#. Retrouver l'adresse réseau en réalisant un ET binaire entre l'adresse IP de la machine et le masque réseau.
#. Combien d'adresses IP sont disponibles pour le réseau ? Combien de machines au plus peut-on connecter au réseau ?
#. La passerelle du réseau est la dernière adresse IP possible. Quelle est son adresse ?

Exercice 2
----------

Bob veut créer un réseau et connecter 4 machines : 2 portables, 1 imprimante et 1 serveur. Le réseau est connecté à
internet avec un routeur.

Il veut sécuriser son réseau en limitant au maximum le nombre de connexions à son réseau, c'est à dire en limitant le
nombre d'adresses IP

#. Combien d'adresses IP au minimum faut-il pour créer le réseau de Bob ?
#. En déduire le masque de réseau qui permet de sécuriser le réseau.
#. L'adresse réseau est ``192.168.0.0``. Attribuer les différentes adresses à chaque machine du réseau.


Exercice 3
----------

.. figure:: ../img/exercice_lan_123.png
   :align: center
   :width: 560

   Routeur et trois réseaux locaux conectés à internet
   
Un routeur muni de 4 interfaces réseau relie 3 réseaux locaux à internet. On dispose des informations suivantes:

-  Le LAN1 a pour adresse réseau ``192.168.0.0/25``
-  Le LAN2 a pour adresse réseau ``10.0.0.0/24``
-  Le LAN3 a pour adresse réseau ``172.16.0.0/16``

On rappelle que l'adresse réseau et l'adresse de diffusion ne sont pas attribuées aux machines du réseau. Elles ne font
pas partie de la plage d'adresses IP que l'on peut attribuer aux machines d'un réseau.

#. Ecrire pour chaque réseau le masque de réseau en décimal.
#. Déterminer pour chaque réseau le nombre d'adresses IP disponibles.
#. Les interfaces réseau du routeur ont pour adresses IP la dernière adresse IP de la plage d'adresses que l'on peut
   attribuer à une machine du réseau. Donner l'adresse IP de la passerelle pour chaque réseau.

Exercice 4
----------

On dispose d'un réseau local constitué d'un portable et d'un serveur DHCP qui appartient au réseau d'adresse IP
``192.168.0.0/24``.

Un fichier *filius* est disponible pour la simulation de ce réseau :download:`simuler un DHCP
<../filius/exercice_dhcp.fls>`.

.. figure:: ../img/exercice_dhcp_lan.png
   :align: center
   :width: 480

#. Quel est le rôle d'un serveur DHCP dans un réseau ? En quoi est-ce avantageux ?
#. L'adresse du portable vous parait-elle correcte ? Pourquoi ?


On démarre le portable et après un court instant, le serveur DHCP lui attribue l'adresse IP ``192.168.0.25``. On
donne les captures des paquets échangés entre le portable et le serveur.

.. figure:: ../img/exercice_dhcp_paquet_1.png
   :align: center
   :width: 400

   Premier paquet échangé

.. figure:: ../img/exercice_dhcp_paquet_2.png
   :align: center
   :width: 400

   Second paquet échangé

.. figure:: ../img/exercice_dhcp_paquet_5.png
   :align: center
   :width: 400

   Troisième paquet échangé

.. figure:: ../img/exercice_dhcp_paquet_6.png
   :align: center
   :width: 400

   Dernier paquet échangé

#. En observant ces paquets, répondre aux questions ci-après.

   a) Quel est le protocole utilisé par la couche application DHCP ?
   b) Quel est le protocole utilisé par la couche transport ?
   c) A quoi correspondent les nombres 67 et 68 ?
   d) Quel est le protocole utilisé par la couche internet ?
   
#. Quelle machine est à l'origine du paquet 1 ? Quelles sont les données envoyées ?
#. Quelle machine est à l'origine du paquet 2 ? Quelles sont les données envoyées ?
#. Quelle machine est à l'origine du paquet 3 ? Quelles sont les données envoyées ?
#. Quelle machine est à l'origine du paquet 4 ? Quelles sont les données envoyées ?
#. Combien de paquets ont été échangés entre le portable et le serveur ? Quels noms peut-on donner à ces échanges ?

