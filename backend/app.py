import json

import requests
from bson import ObjectId, json_util
from Database import Database
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)


GOOGLE_MAPS_API_KEY = ""

myDb = Database()


@app.route("/")
def index():
    return render_template("index.html")


# Endpoint pour ajouter un historique
@app.route("/historique", methods=["POST"])
def add_historique():
    data = request.json
    insert_historique = myDb.add_data_historique(
        data.get("id_poubelle"),
        data.get("coef_touristes"),
        data.get("date"),
        data.get("niveau_remplissage"),
    )
    if insert_historique:
        return jsonify({"message": "Historique ajouté avec succès"})
    return jsonify({"message": "Erreur lors de l'ajout de l'historique"}), 500


# Endpoint pour recuperer l'historique des collectes
@app.route("/historique", methods=["GET"])
def get_data_historique():
    historique = myDb.get_data_historique()
    historique_list = []
    for collecte in historique:
        collecte["_id"] = str(collecte["_id"])
        historique_list.append(collecte)
    return jsonify({"historique": historique_list})


@app.route("/historique/<historique_id>", methods=["GET"])
def get_data_historique_by_id(id):
    historique = myDb.get_data_historique_by_id(id)
    if historique:
        historique["_id"] = str(historique["_id"])
        return jsonify({"historique": historique})
    return jsonify({"message": "Historique non trouvé"}), 404


@app.route("/historique/<historique_id>", methods=["PUT"])
def update_historique(historique_id):
    data = request.json
    update_historique = myDb.update_data_historique(
        historique_id,
        data.get("id_poubelle"),
        data.get("coef_touristes"),
        data.get("date"),
        data.get("niveau_remplissage"),
    )
    if update_historique.modified_count > 0:
        return jsonify({"message": "Historique mis à jour avec succès"})
    return (
        jsonify({"message": "Historique non trouvé ou aucune modification effectuée"}),
        404,
    )


# Endpoint pour supprimer l'historique des collectes
@app.route("/historique/<historique_id>", methods=["DELETE"])
def delete_historique(historique_id):
    result = myDb.delete_data_historique(historique_id)
    if result.deleted_count > 0:
        return jsonify({"message": "Historique supprimé avec succès"})
    return jsonify({"message": "Historique non trouvé"}), 404


# Endpoint pour ajouter un trajet
@app.route("/trajets", methods=["POST"])
def add_trajet():
    data = request.json
    insert_trajet = myDb.add_data_trajet(
        data.get("id_collecteur"),
        data.get("id_poubelle"),
        data.get("date"),
        data.get("niveau_remplissage"),
    )
    if insert_trajet:
        return jsonify({"message": "Trajet ajouté avec succès"})
    return jsonify({"message": "Erreur lors de l'ajout du trajet"}), 500


# Endpoint pour supprimer les trajets
@app.route("/trajets/<trajet_id>", methods=["DELETE"])
def delete_trajet(trajet_id):
    result = myDb.delete_data_trajet(trajet_id)
    if result.deleted_count > 0:
        return jsonify({"message": "Trajet supprimé avec succès"})
    return jsonify({"message": "Trajet non trouvé"}), 404


@app.route("/trajets/<trajet_id>", methods=["PUT"])
def update_trajet(trajet_id):
    data = request.json
    update_trajet = myDb.update_data_trajet(
        trajet_id,
        data.get("id_collecteur"),
        data.get("id_poubelle"),
        data.get("date"),
        data.get("niveau_remplissage"),
    )
    if insert_trajet:
        return jsonify({"message": "Trajet ajouté avec succès"})
    return jsonify({"message": "Erreur lors de l'ajout du trajet"}), 500


# Endpoint pour supprimer les trajets
@app.route("/trajets/<trajet_id>", methods=["DELETE"])
def delete_trajet(trajet_id):
    result = myDb.delete_data_trajet(trajet_id)
    if result.deleted_count > 0:
        return jsonify({"message": "Trajet supprimé avec succès"})
    return jsonify({"message": "Trajet non trouvé"}), 404


@app.route("/trajets/<trajet_id>", methods=["PUT"])
def update_trajet(trajet_id):
    data = request.json
    update_trajet = myDb.update_data_trajet(
        trajet_id,
        data.get("id_collecteur"),
        data.get("id_poubelle"),
        data.get("date"),
        data.get("niveau_remplissage"),
    )
    if update_trajet.modified_count > 0:
        return jsonify({"message": "Trajet mis à jour avec succès"})
    return (
        jsonify({"message": "Trajet non trouvé ou aucune modification effectuée"}),
        404,
    )


# Endpoint pour recuperer les trajets
@app.route("/trajets", methods=["GET"])
def get_data_trajets():
    trajets = myDb.get_data_trajet()
    trajets_list = []
    for trajet in trajets:
        trajet["_id"] = str(trajet["_id"])
        trajets_list.append(trajet)
    return jsonify({"trajets": trajets_list})


@app.route("/trajets/<trajet_id>", methods=["GET"])
def get_data_trajet_by_id(id):
    trajet = myDb.get_data_trajet_by_id(id)
    if trajet:
        trajet["_id"] = str(trajet["_id"])
        trajets_list.append(trajet)
    return jsonify({"trajets": trajets_list})


@app.route("/trajets/<trajet_id>", methods=["GET"])
def get_data_trajet_by_id(id):
    trajet = myDb.get_data_trajet_by_id(id)
    if trajet:
        trajet["_id"] = str(trajet["_id"])
        return jsonify({"trajet": trajet})
    return jsonify({"message": "Trajet non trouvé"}), 404


# Endpoint pour ajouter une zone
@app.route("/zones", methods=["POST"])
def add_zone():
    data = request.json
    insert_zone = myDb.add_data_zone(
        data.get("nom"),
        data.get("densité"),
        data.get("gps"),
        data.get("nb_poubelles"),
    )
    if insert_zone:
        return jsonify({"message": "Zone ajoutée avec succès"})
    return jsonify({"message": "Erreur lors de l'ajout de la zone"}), 500


# Endpoint pour obtenir les zones
@app.route("/zones", methods=["GET"])
def get_zones():
    zones = myDb.get_data_zone()
    zone_list = []
    for zone in zones:
        zone["_id"] = str(zone["_id"])
        zone_list.append(zone)
    return jsonify(zone_list)


# Endpoint pour obtenir une zone spécifique
@app.route("/zones/<zone_id>", methods=["GET"])
def get_zone(zone_id):
    zone = myDb.get_data_zone_by_id({"_id": ObjectId(zone_id)})
    if zone:
        zone["_id"] = str(zone["_id"])
        return jsonify({"zone": zone})
    return jsonify({"message": "Zone non trouvée"}), 404


# Endpoint pour update une zone specifiques
@app.route("/zones/<zone_id>", methods=["PUT"])
def update_zone(zone_id):
    data = request.json
    update_zone = myDb.update_data_zone(
        zone_id,
        data.get("nom"),
        data.get("densite"),
        data.get("gps"),
        data.get("nb_poubelles"),
    )
    if update_zone.modified_count > 0:
        return jsonify({"message": "Zone mis à jour avec succès"})
    return (
        jsonify({"message": "Zone non trouvée ou aucune modification effectuée"}),
        404,
    )


# Endpoint pour la suppression d'une zone
@app.route("/zones/<zone_id>", methods=["DELETE"])
def delete_zone(zone_id):
    result = myDb.delete_data_zone(zone_id)
    if result.deleted_count > 0:
        return jsonify({"message": "Zone supprimée avec succès"})
    return jsonify({"message": "Zone non trouvée"}), 404


# Endpoint pour ajouter une poubelle
@app.route("/poubelles", methods=["POST"])
def add_poubelle():
    data = request.json
    insert_poubelle = myDb.add_data_poubelle(
        data.get("gps"),
        data.get("niveau_remplissage"),
        data.get("coefficient_touriste"),
        data.get("densite_population"),
    )
    if insert_poubelle:
        return jsonify({"message": "Poubelle ajoutée avec succès"})
    return jsonify({"message": "Erreur lors de l'ajout de la poubelle"}), 500


# Endpoint pour obtenir les poubelles d'une zonze donnée
@app.route("/zones/<zone_id>/poubelles", methods=["GET"])
def get_poubelles(zone_id):
    poubelles = myDb.get_data_poubelle_by_zone(zone_id)
    poubelle_list = []
    for poubelle in poubelles:
        poubelle["_id"] = str(poubelle["_id"])
        poubelle_list.append(poubelle)
    return jsonify({"poubelles": poubelle_list})


# Endpoint pour obtenur les informations d'une poubelle donnée
@app.route("/poubelles", methods=["GET"])
# Endpoint pour obtenur la liste des poubelles
@app.route("/poubelles", methods=["GET"])
def get_all_poubelles():
    poubelles = myDb.get_data_poubelle()

    return json.loads(json_util.dumps(poubelles))


# Endpoint pour obtenur les informations d'une poubelle donnée
@app.route("/poubelles/<poubelle_id>", methods=["GET"])
def get_poubelle(poubelle_id):
    poubelle = myDb.get_data_poubelle_by_id(poubelle_id)
    if poubelle:
        poubelle["_id"] = str(poubelle["_id"])
        return jsonify({"poubelle": poubelle})
    return jsonify({"message": "Poubelle non trouvée"}), 404


# Endpoint pour update une poubelle specifiques
@app.route("/poubelles/<poubelle_id>", methods=["PUT"])
def update_poubelle(poubelle_id):
    data = request.json
    update_poubelle = myDb.update_data_poubelle(
        poubelle_id,
        data.get("coefficient_touriste"),
        data.get("densite"),
        data.get("next_collection_date"),
    )
    if update_poubelle.modified_count > 0:
        return jsonify({"message": "Poubelle mis à jour avec succès"})
    return (
        jsonify({"message": "Poubelle non trouvée ou aucune modification effectuée"}),
        404,
    )


# Endapoint pour la suppression d'une poubelle
@app.route("/poubelles/<poubelle_id>", methods=["DELETE"])
def delete_poubelle(poubelle_id):
    result = myDb.delete_data_poubelle(poubelle_id)
    if result.deleted_count > 0:
        return jsonify({"message": "Poubelle supprimée avec succès"})
    return jsonify({"message": "Poubelle non trouvée"}), 404


# Endpoint pour ajouter un collecteur
@app.route("/collecteurs", methods=["POST"])
def add_collecteur():
    data = request.json
    insert_collecteur = myDb.add_data_collecteur(
        data.get("id_zone"),
        data.get("matricule"),
        data.get("nom"),
        data.get("prenom"),
        data.get("username"),
        data.get("password"),
        data.get("role"),
    )

    print("insert_collecteur", insert_collecteur)
    if insert_collecteur:
        return jsonify({"message": "Collecteur ajouté avec succès"})
    return jsonify({"message": "Erreur lors de l'ajout du collecteur"}), 500


# Endpoint pour obtenir la liste de tous les collecteurs
@app.route("/collecteurs", methods=["GET"])
def get_all_collecteurs():
    collecteurs = myDb.get_data_collecteur()
    collecteur_list = []
    for collecteur in collecteurs:
        collecteur["_id"] = str(collecteur["_id"])
        collecteur_list.append(collecteur)
    return jsonify({"collecteurs": collecteur_list})


# Endpoint pour obtenir les informations d'un collecteur donné
@app.route("/collecteurs/<collecteur_id>", methods=["GET"])
def get_collecteur(collecteur_id):
    collecteur = myDb.get_data_collecteur_by_id(collecteur_id)
    if collecteur:
        collecteur["_id"] = str(collecteur["_id"])
        return jsonify({"collecteur": collecteur})
    return jsonify({"message": "Collecteur non trouvé"}), 404


@app.route("/collecteurs/zone/<id_zone>", methods=["GET"])
def get_data_collecteur_by_zone(id_zone):
    collecteur = myDb.get_data_collecteur_by_zone(id_zone)
    if collecteur:
        collecteur["_id"] = str(collecteur["_id"])
        return jsonify({"collecteur": collecteur})
    return jsonify({"message": "Collecteur non trouvé"}), 404


@app.route("/collecteurs/zone/<id_zone>", methods=["GET"])
def get_data_collecteur_by_zone(id_zone):
    collecteur = myDb.get_data_collecteur_by_zone(id_zone)
    if collecteur:
        collecteur["_id"] = str(collecteur["_id"])
        return jsonify({"collecteur": collecteur})
    return jsonify({"message": "Collecteur non trouvé"}), 404


# Endpoint pour update un collecteur specifiques
@app.route("/collecteurs/<collecteur_id>", methods=["PUT"])
def update_collecteur(collecteur_id):
    data = request.json
    updated_data = myDb.update_data_collecteur(
        collecteur_id,
        data.get("matricule"),
        data.get("nom"),
        data.get("prenom"),
        data.get("username"),
        data.get("password"),
        data.get("role"),
    )
    if updated_data.modified_count > 0:
        return jsonify({"message": "Collecteur mis à jour avec succès"})
    return (
        jsonify({"message": "Collecteur non trouvé ou aucune modification effectuée"}),
        404,
    )


# Endpoint pour la suppression d'un collecteur
@app.route("/collecteurs/<collecteur_id>", methods=["DELETE"])
def delete_collecteur(collecteur_id):
    result = myDb.delete_data_collecteur(collecteur_id)
    if result.deleted_count > 0:
        return jsonify({"message": "Collecteur supprimé avec succès"})
    return jsonify({"message": "Collecteur non trouvé"}), 404


@app.route("/get_directions", methods=["GET"])
def get_directions():
    try:
        origin = "40.748817,-73.985428"

        destination = "34.052235,-118.243683"

        api_url = "https://maps.googleapis.com/maps/api/directions/json"
        params = {
            "origin": origin,
            "destination": destination,
            "key": GOOGLE_MAPS_API_KEY,
        }

        response = requests.get(api_url, params=params)
        data = response.json()

        routes = data.get("routes", [])
        if routes:
            route = routes[0]
            distance = route.get("legs")[0].get("distance").get("text")
            duration = route.get("legs")[0].get("duration").get("text")
            steps = route.get("legs")[0].get("steps")

            # Retourner les informations sous forme de JSON
            return jsonify(
                {
                    "success": True,
                    "distance": distance,
                    "duration": duration,
                    "steps": steps,
                }
            )
        else:
            return jsonify({"success": False, "error": "Aucun itinéraire trouvé"})

    except Exception as e:
        return jsonify({"success": False, "error": str(e)})


if __name__ == "__main__":
    app.run(debug=True)
