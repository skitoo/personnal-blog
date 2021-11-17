---
Title: Logger toutes les exceptions en Python
Date: 2014-05-27
Icon: python
Tags: [Code]
Url: "/logger-toutes-les-exceptions-en-python.html"

---

Si comme moi vous travaillez sur des projets ayant une taille conséquante il peut être intéressant de logger l'ensemble des exceptions à l'aide du logger Python. Seulement mettre des try/except dans le moindre recoin de votre code peut rapidement être fastidieux et rend votre code vite illisible.

En python, comme dans d'autre langage de programmation, il existe un moyen simple de faire cela une fois pour toutes : dans notre cas, la fonction [sys.excepthook](https://docs.python.org/2/library/sys.html#sys.excepthook)

```python
import sys
import logging
import traceback as tb

logger = logging.getLogger(__name__)

def log_exception_hook(type, value, traceback):
    logger.error(''.join(tb.format_tb(traceback)))
    logger.error('{0} - {1}'.format(type, value))

sys.excepthook = log_exception_hook
```

En cas d'exception la fonction *log_exception_hook* sera appelée. Le premier paramètre est la classe de l'exception, le second est l'objet exception et enfin le troisième le traceback que l'exception à produite.
