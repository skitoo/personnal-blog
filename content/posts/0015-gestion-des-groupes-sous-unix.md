---
Title: Gestion des groupes sous Linux
Date: 2014-06-05
Icon: groups-friends
Tags: [Système]
Url: "/gestion-des-groupes-sous-linux.html"

---

La gestion des groupes sous **Linux** est quelque chose que je pratique rarement. Je profite donc de cet article pour rappeler comment cela se gère.

## Création d'un groupe utilisateur

Pour cela rien de très compliqué :

```bash
groupadd <nomdugroupe>
```

## Suppression d'un groupe utilisateur

Très simple également :

```bash
groupdel <nomdugroupe>
```

## Ajout d'un utilisateur dans un groupe

Une fois que votre groupe est créé, on peut ajouter des utilisateurs à celui-ci. Plusieurs façon d'opérer :

```bash
usermod -a -G <nomdugroupe> <utilisateur>
```

L'option **-a** indique que c'est un ajout. L'option **-G** indique que c'est pour un groupe.

La seconde manière de réaliser cela :

```bash
gpasswd -a <utilisateur> <nomdugroupe>
```

## Supprimer un utilisateur d'un groupe

Pour la suppression, là aussi, plusieurs manières de réaliser cette action :

```bash
gpasswd -d <utilisateur> <nomdugroupe>
```

où

```bash
deluser <utilisateur> <nomdugroupe>
```

## Liste des groupes

Voici le moyen de connaître les groupes d'un utilisateur

```bash
groups <utilisateur>
```

Et de l'ensemble du système

```bash
groups
```


## Liste des utilisateurs présents dans un groupe

Enfin voici la commande qui vous permet d'afficher les utilisateurs d'un groupe

```bash
getent group <nomdugroupe>
```
