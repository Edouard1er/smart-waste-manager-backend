import requests
from flask import Flask, jsonify, render_template
from redis import Redis

app = Flask(__name__)
redis = Redis(host="localhost", port=6379)


@app.route("/")
def testwithredis():
    redis.incr("hits")
    return "Nombre de visites : {}".format(redis.get("hits").decode("utf-8"))


GOOGLE_MAPS_API_KEY = ""


@app.route("/")
def index():
    return render_template("index.html")


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
