# My personnal blog

The source code of [my personnal blog](http://www.skitoo.net) make with [Pelican](http://blog.getpelican.com/) and :heart:.

[![Licence GPL](http://img.shields.io/badge/license-GPL-yellow.svg)](http://www.gnu.org/licenses/quick-guide-gplv3.fr.html)

## Dependencies

My blog relies on several outside packages and programs to run.

* [Python 2.7](https://python.org)
* [Pelican](http://blog.getpelican.com/)
* [Docker](https://docker.com)
* [Docker Compose](https://docs.docker.com/compose/overview/)

## Quick start

Clone the project

```
$ git@github.com:skitoo/personnal-blog.git
$ cd personnal-blog
```

Run docker-compose

```
$ docker-compose up
```

Add entry in your `/etc/hosts` file:

```
127.0.0.1 localhost local.skitoo.net
```

And you can go to the following url with your favorite browser: [https://local.skitoo.net](https://local.skitoo.net)

If you edit a file, pelican regenerate for you the site.

## LICENSE

[GNU GENERAL PUBLIC LICENSE Version 3](http://www.gnu.org/licenses/gpl-3.0.txt)
