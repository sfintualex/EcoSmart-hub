# Importăm bibliotecile necesare
from flask import Flask, jsonify, request, send_from_directory

app = Flask(__name__)

# Simulăm o bază de date pentru 3 utilizatori
users_data = {
    "user1": {
        "consum": [
            {"data": "2025-01-01", "energie": 10, "apa": 5, "gaze": 3},
            {"data": "2025-01-02", "energie": 8, "apa": 4, "gaze": 2}
        ]
    },
    "user2": {
        "consum": [
            {"data": "2025-01-01", "energie": 15, "apa": 7, "gaze": 6}
        ]
    },
    "user3": {
        "consum": []
    }
}

# Ruta pentru servirea paginii HTML principale
@app.route("/", methods=["GET"])
def index():
    return send_from_directory(".", "index.html")

# Ruta pentru servirea paginii hub
@app.route("/hub.html", methods=["GET"])
def hub():
    return send_from_directory(".", "hub.html")

# Ruta pentru servirea paginii consum
@app.route("/consum.html", methods=["GET"])
def consum_page():
    return send_from_directory(".", "consum.html")

# Ruta pentru servirea paginii adaugă consum
@app.route("/adauga_consum.html", methods=["GET"])
def adauga_consum_page():
    return send_from_directory(".", "adauga_consum.html")

# Ruta pentru servirea paginii recomandări
@app.route("/recomandari.html", methods=["GET"])
def recomandari_page():
    return send_from_directory(".", "recomandari.html")

# Ruta pentru obținerea consumului unui utilizator
@app.route("/api/consum/<username>", methods=["GET"])
def get_consum(username):
    user = users_data.get(username)
    if not user:
        return jsonify({"error": "Utilizatorul nu există."}), 404
    return jsonify({"consum": user["consum"]})

# Ruta pentru adăugarea unui nou consum
@app.route("/api/consum/<username>", methods=["POST"])
def add_consum(username):
    user = users_data.get(username)
    if not user:
        return jsonify({"error": "Utilizatorul nu există."}), 404

    data = request.json
    if not data or not all(key in data for key in ["energie", "apa", "gaze"]):
        return jsonify({"error": "Date invalide."}), 400

    new_entry = {
        "data": "2025-01-13",  # Data poate fi generată dinamic
        "energie": data["energie"],
        "apa": data["apa"],
        "gaze": data["gaze"]
    }
    user["consum"].append(new_entry)
    return jsonify({"mesaj": "Consum adăugat cu succes."})

# Ruta pentru obținerea recomandărilor unui utilizator
@app.route("/api/recomandari/<username>", methods=["GET"])
def get_recomandari(username):
    user = users_data.get(username)
    if not user:
        return jsonify({"error": "Utilizatorul nu există."}), 404

    recomandari = [
        "Reduceti utilizarea aparatelor electrice neesentiale.",
        "Inchideti robinetul cand nu folositi apa.",
        "Optati pentru becuri LED pentru economisirea energiei."
    ]
    return jsonify({"recomandari": recomandari})

if __name__ == "__main__":
    app.run(debug=True)
