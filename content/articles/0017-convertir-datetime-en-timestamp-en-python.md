Title: Convertir un objet datetime Python en timestamp
Date: 2014-07-09 18:00
Icon: python
Tags: Code


Voila un truc que j'arrive jamais à me souvenir : comment convertir un objet **datetime** **Python** en **timestamp**.

Voici le petit bout de code qui permet de faire ça :

	::python
    import datetime
    import time

    now = datetime.datetime.now()  # on récupère la date actuelle
    timestamp = time.mktime(now.timetuple())  # on effectue la convertion

Voila ! Vous l'aurez compris c'est très simple mais il faut s'en souvenir :)

Pour la peine je vous donne la convertion dans l'autre sens : de timestamp vers datetime.

	::python
    import datetime

    timestamp = 1404900633
    dt = datetime.datetime.fromtimestamp(timestamp)


