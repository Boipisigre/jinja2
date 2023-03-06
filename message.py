# write_messages.py

from jinja2 import Environment, FileSystemLoader

max_score = 100
test_name = "Python Challenge"
students = [
    {"name": "Sandrine",  "score": 100},
    {"name": "Gergeley", "score": 87},
    {"name": "Frieda", "score": 92},
]

# positionnement du répertoire de modèle.
environment = Environment(loader=FileSystemLoader("templates/"))

# chargement du fichier modèle
template = environment.get_template("message.txt")

# Boucle sur les étudiants
for student in students:
    filename = f"output/message_{student['name'].lower()}.txt"

    # Effectuer le rendu du modèle
    content = template.render(
        student,
        max_score=max_score,
        test_name=test_name
    )
    with open(filename, mode="w", encoding="utf-8") as message:
        message.write(content)
        print(f"... wrote {filename}")
