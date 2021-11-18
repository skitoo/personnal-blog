---
Title: Comment résoudre l'erreur "wxe_driver.so" sous Elixir
Date: 2017-10-26
Icon: terminal
Tags: [Code]
Url: "/comment-resoudre-lerreur-wxe_driverso-sous-elixir.html"

---


Dans le langage Elixir il est fourni un super outil pour debugger et visualiser l'ensemble des processus dans votre programme.

Pour cela, il suffit de lancer la commande suivante dans votre console iex :

```elixir
:observer.start
# ou
:debugger.start
```

Sauf que voilà, sous Archlinux, les dépendances, pour cette fonctionnalité, ne sont pas installé par défaut avec Elixir et vous risquez de rencontrer l'erreur suivante :

```
[error] ERROR: Could not find 'wxe_driver.so' in: /usr/lib/erlang/lib/wx-1.8.1/priv
```

Pour remédier à cela, il suffit d'installer le package suivant :

```shell
sudo pacman -S erlang
```

Rien d'étonnant à cela, le langage Elixir tourne sur la machine virtuelle de Erlang.
De base Elixir s'appui sur le paquet `erlang-nox` : une version d'Erlang sans gestion du système Window X. Il est donc nécessaire de le remplacer par le paquet qui inclut ce système.

Pour pouvez désormais profiter de votre debugger !
