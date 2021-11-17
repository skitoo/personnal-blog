---
Title: Arduino !
Date: 2010-10-12
Icon: diode
Tags: [Electronique]
Url: "/arduino.html"

---

Suite à [mon précédent billet](http://www.skitoo.net/vaisseau-spatial-fait-maison.html), j'ai commencé une réflexion concernant
la mise en œuvre d'un projet similaire. Beaucoup de paramètres sont à
prendre en compte notamment sur la partie technique. Dans la vidéo, le
système embarqué est une caméra HD ainsi qu'un Iphone permettant de
retrouver l'appareil après sa chute. Le coût d'un tel dispositif est non
négligeable, surtout si l'on ne parvient pas à retrouver l'engin...
Ayant fait une partie de mes études dans le domaine de l'électricité
(cela remonte à pas mal de temps :D), une idée m'est venue à l'esprit : Pourquoi ne pas réaliser soi-même ce système embarqué ? Un peu fou ? Peut-être...
J'ai donc lancé mes recherches en commençant par les [microcontroleurs](http://fr.wikipedia.org/wiki/Microcontroleur). Après
avoir passé en revu quelques systèmes très connus dans le domaine (comme
les [PIC](http://fr.wikipedia.org/wiki/Microcontrôleur_PIC)), je me suis aperçu qu'ils pouvaient être assez complexe à
utiliser et à programmer : langage Assembleur, environnement de
développement sous Windows... Un autre point négatif : leurs coûts peuvent être élevés surtout si l'on
ajoute celui du programmateur. En creusant un peu plus j'ai
découvert un système plus adapté à mon niveau et à mon budget: le
circuit imprimé [Arduino](http://arduino.cc/).

![Arduino](/images/arduino_uno_test.jpg)

Ce montage intègre un microcontroleur ainsi que son programmateur. Il se
branche sur votre ordinateur via une interface USB. Le module est
compatible avec tous les systèmes d'exploitations couramment utilisés :
Windows, Mac Os X et Linux.

Arduino est un système totalement Open Source, autant sur la partie
software que hardware ! Le langage utilisé est tout simplement
"Arduino", un dérivé du C. Il est d'ailleurs facilement extensible avec
ce dernier.

Un autre point positif est que cette petite bête est fournie avec un
ensemble d'exemples permettant d'appréhender rapidement la programmation
et le montage du module : chenillard de LED, contrôle d'un servomoteur,
communication avec l'ordinateur... etc (pour voir quelques exemples et
projet plus avancés, je vous conseille un petit tour sur Youtube avec le
mot clé "arduino")

Une fois votre programme chargé dans le cœur du microcontroleur, vous
pouvez bien-sûr rendre le circuit imprimé totalement autonome en
débranchant le câble USB de votre ordinateur. Une source d'énergie est
bien entendu nécessaire.

J'ai donc commandé le module ce week-end sur le site [Lextronic](http://lextronic.fr/) afin
de commencer quelques expérimentations ! Je publierai peut-être quelques
tests :)
