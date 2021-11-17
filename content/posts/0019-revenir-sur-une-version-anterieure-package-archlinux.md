---
Title: Revenir sur une version antérieure d'un package Archlinux
Date: 2016-06-09
Icon: terminal
Tags: [Système]
Url: "/revenir-sur-une-version-anterieure-dun-package-archlinux.html"

---

J'ai récemment dû faire un "downgrade" d'un paquet Archlinux car la version actuelle me posait quelques soucis. Après une recherche sur les internets infructueuse, mon pote [Benoît](http://benoitbar.fr/) m'a parlé d'un outil qui permet de réaliser rapidement et simplement cette action : [agetpkg](https://github.com/seblu/agetpkg).


Pour commencer, vous devez installer cet outil :

```shell
$ yaourt agetpkg
```

Vous remarquerez qu'à ce jour, yaourt va piocher directement sur le github du projet.

Une fois installé il suffit de taper la commande suivante pour pouvoir choisir la version du paquet souhaitée (dans mon cas : docker-compose version 1.5.2)


```shell
$ agetpkg -i docker-compose 1.5.2
0 docker-compose-1.5.2-1-x86_64.pkg.tar.xz
1 docker-compose-1.5.2-2-x86_64.pkg.tar.xz
Select packages (* for all):
```

Dans mon cas il me propose plusieurs "sous-versions" du paquet.

Et voilà ! Votre "nouvelle" version du paquet est installée !
