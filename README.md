# Introduction à la création de modèles Jinja

## Premiers pas

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

print(template.render(name="World"))


Il est biensur plus intéressant de charger un modèle à partir d'un fichier.
