Title: Modifier l'extension d'une url avec NginX
Date: 2016-01-10
Icon: terminal
Tags: Système

Dans le cas présent, je souhaiterais rediriger tous les appels aux url finissant par ```*.html``` vers la même url mais sans extension.

Exemple :
`www.skitoo.net/unepage.html` vers `www.skitoo.net/unepage/`

Pour celà voici la petite astuce qui permet de réaliser cette redirection :

```nginx
    location ~ \.html$ {
        rewrite ^/(.*)\.html$ /$1 last;
    }
```


[Source](http://linuxaria.com/pills/how-to-modify-an-url-extension-with-a-nginx-rewrite)
