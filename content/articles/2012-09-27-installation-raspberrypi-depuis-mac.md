Title: Tutoriel RaspberryPi : Créer une carte SD depuis votre Mac
Date: 2012-09-26 10:20
Icon: icon-beaker
Status: draft

Comme je vous le signalais lors d'un précédent article je me suis récemment offert un [Raspberry PI](/raspberry-pi-lordinateur-a-bas-cout.html). Voici aujourd'hui quelques lignes pour vous expliquer comment installer sur votre carte SD le système d'exploitation depuis votre Mac.

##Téléchargement de l'image

Avant toute chose il vous sera nécéssaire de télécharger l'image en vous rendant sur [la page prévue à cet effet](http://www.raspberrypi.org/downloads).

Plusieurs distributions vous sont proposées. Pour ma part j'ai fait le choix qui est recommandé par les développeurs c'est à dire la *Raspbian “wheezy”*.

![RaspberryPi Download Page](/images/raspberrypi-download-page.png)

Comme vous pouvez le constater 2 possibilités s'offrent à vous soit le téléchargement direct soit via Torrent. A vous de choisir le mode qui vous convient le mieux. 

Vous remarquerez la présence d'un code SHA-1, ce dernier va vous être utile pour savoir si l'image que vous venez de télécharger n'a pas été endommagé pendant le téléchargement.

Une fois votre téléchargement terminé, lancez un Terminal (Applications -> Utilitaires -> Terminal), déplacez vous dans le dossier où se trouve votre fichier (pour ma part le bureau) puis on lance une commande de contrôle de l'image : 

<pre><code data-language="bash"># on se déplace dans le dossier
$ cd ~/Desktop/

# on lance le contrôle de l'image
$ openssl sha1 2012-09-18-wheezy-raspbian.zip
SHA1(2012-09-18-wheezy-raspbian.zip)= 3bc788d447bc88feaae8382d61364eaba1088e78
</code></pre>

Si le code affiché par cette commande correspond à celui donné par la page de téléchargement du site vous pouvez passer à l'étape suivante dans le cas contraire vous êtes bon pour re-télécharger le fichier.

##

