# write_messages.py

from jinja2 import Environment, FileSystemLoader

max_score = 100
test_name = "Python Challenge"
students = [
    {"name": "Sandrine",  "score": 100},
    {"name": "Gergeley", "score": 87},
    {"name": "Frieda", "score": 92},
    {"name": "Fritz", "score": 40},
    {"name": "Sirius", "score": 75},
]

# positionnement du répertoire de modèle.
environment = Environment(loader=FileSystemLoader("templates/"))

# chargement du fichier modèle
template = environment.get_template("messageif.txt")

# Boucle sur les étudiants
for student in students:
    filename = f"output/messageif_{student['name'].lower()}.txt"

    # Effectuer le rendu du modèle
    content = template.render(
        student,
        max_score=max_score,
        test_name=test_name
    )
    with open(filename, mode="w", encoding="utf-8") as message:
        message.write(content)
        print(f"... wrote {filename}")

# gestion du rendu dans le modèle
results_filename = "output/students_results.html"
results_template = environment.get_template("resultat.html")
context = {
    "students": students,
    "test_name": test_name,
    "max_score": max_score,
}
with open(results_filename, mode="w", encoding="utf-8") as results:
    results.write(results_template.render(context))
    print(f"... wrote {results_filename}")
