---
Title: "error: key could not be looked up remotely"
Date: 2017-10-24
Icon: archlinux
Tags: [Système]
Url: "/error-key-could-not-be-looked-up-remotely.html"

---


Voilà 2 ans que j'utilise quotidiennement la distribution Linux Archlinux. Mais ce matin, un petit souci vient enrayer mon enthousiasme... Lors d'une tentative de mise à jour des paquets via pacman, une erreur s'est produite :

```shell
$ sudo pacman -Syu
:: Synchronizing package databases...
 core is up to date
 extra is up to date
 community is up to date
 multilib is up to date
....
....
....
downloading required keys...
error: key "EEEEE2EEEE2EEEEE" could not be looked up remotely
error: required key missing from keyring
error: failed to commit transaction (unexpected error)
Errors occurred, no packages were upgraded.
```

Un soucis sur une clé qui semble ne plus être disponible dans le trousseau...

Après quelques recherches, j'ai finalement réussi à trouver une solution pour résoudre ce problème :

```shell
$ rm -R /etc/pacman.d/gnupg/
$ rm -R /root/.gnupg/  # uniquement si le dossier existe
$ gpg --refresh-keys
$ pacman-key --init && pacman-key --populate
$ pacman-key --refresh-keys
```

Voilà ! Vous pouvez relancer la commande d'upgrade de vos paquets !
