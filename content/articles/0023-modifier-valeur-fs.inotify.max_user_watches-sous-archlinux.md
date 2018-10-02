Title: Modifier la valeur fs.inotify.max_user_watches sous Archlinux
Date: 2017-10-31
Icon: archlinux
Tags: Système


Si vous travaillez avec des outils comme Webpack, vous utilisez certainement l'option watch qui permet de lancer automatiquement la compilation de votre code dès que vous modifiez un des fichiers de votre projet.

Pour fonctionner, Webpack (et tous les outils de ce style) utilise le système d'événement de votre système d'exploitation. A savoir sous linux : inotify.

Sauf que sur des projets contenant un nombre important de fichiers, il peut arriver que la base de données de inotify ne veuille plus se mettre à jour.

Pour remédier à cela, il faut modifier l'option fs.inotify.max_user_watches de inotify en augmentant sa valeur.
Cette option permet de demander au noyau Linux d'augmenter le nombre d'entrées que inotify peut créer.

Pour cela, rien de très compliqué :

On édite le fichier /usr/lib/sysctl.d/90-override.conf. Si il n'existe pas, vous devez le créer.

```shell
$ vim /usr/lib/sysctl.d/90-override.conf
```

Et vous y placer la ligne suivante :

```
fs.inotify.max_user_watches = 100000
```

Après avoir édité le fichier il faut recharger la configuration avec sysctl :

```shell
$ sysctl --system
```

Et voilà ! Normalement vous ne devriez plus avoir le souci.

