from flask import Flask, render_template, request
import random

app = Flask(__name__)

# Liste des couleurs préférées
colors = ["black", "red", "#0000FF", "#FF9900"]

# Chemin vers le fichier shot.txt
shot_file_path = "shot.txt"

# Fonction pour lire une ligne aléatoire à partir du fichier shot.txt
def get_random_shot():
    with open(shot_file_path, 'r') as file:
        lines = file.readlines()
        return random.choice(lines).strip()

@app.route('/')
def index():
    # Choisir une couleur aléatoire pour chaque élément de style
    color1, color2, color3 = random.sample(colors, 3)
    return render_template('index.html', color1=color1, color2=color2, color3=color3)

@app.route('/get_random_line', methods=['POST'])
def get_random_line():
        random_line = get_random_shot()
        return render_template('random_line.html', random_line=random_line)
if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=False)