# Introduction à la création de modèles Jinja

## Premiers pas
construit à partir de https://realpython.com/primer-on-jinja-templating/
### installation
> pipenv install Jinja2

### Vérification
> pipenv graph
Jinja2==3.1.2
  - MarkupSafe [required: >=2.0, installed: 2.1.2]
pkg-resources==0.0.0

**Nota** : si l'installation se fait avec Jinja2 l'import lui doit se faire avec jinja2.

> Python 3.9.2 (default, Feb 28 2021, 17:03:44)
[GCC 10.2.1 20210110] on linux
Type "help", "copyright", "credits" or "license" for more information.
>> import Jinja2   
Traceback (most recent call last):   
  File "<stdin>", line 1, in <module>    
ModuleNotFoundError: No module named 'Jinja2'   
>> import jinja2

### Premier test

>import jinja2  
environment = jinja2.Environment()  
template = environment.from_string("Hello, {{ name }}!")  
print(template.render(name="World"))


Dans ce premier code on voit les bases de jinja2 .

le chargement d'un modèle dans le moteur (environnemt).

> template = environment.from_string("Hello, {{ name }}!")

le rendu

> print(template.render(name="World"))


Il est bien sur plus intéressant de charger un modèle à partir d'un fichier.

## Aller plus loin

### Un fichier comme modèle:
 voici le fichier modèle : message.txt

 > {# templates/message.txt #}
>
> Bonjour {{ name }}!
>
>  Je suis heureux de vous informer que vous avez très bien réussi l'examen d'aujourd'hui : {{ test_name }}.   
 Vous avez atteint {{ score }} sur {{ max_score }} points.
>
>  A bientôt!
>     
 >Pierre


le script message.py montre comment on charge un modèle et l'on utilise les variables {{ nom }} dans jinja2.

**Nota** : on passe la structure student et non pas name et score


### Maîtriser le flux dans Jinja

Dans jinja2 il existe des structures de programmation permettant de traiter des cycles, des conditions.

#### Instruction if

Elle fonctionne comme en Python

la syntaxe est proche
{% if %}
   action
{% else %}
   action
{% endif %}

#### Instruction loop

c'est en fait l'instruction {% for %} elle aussi construite comme en Python..
