import urllib.request
import json
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def get_list_characters_page():
    url = "https://rickandmortyapi.com/api/character"
    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)

    return render_template("characters.html", characters=dict["results"])


@app.route("/profile/<id>")
def get_profile(id):
    url = "https://rickandmortyapi.com/api/character/" + id
    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)

    return render_template("profile.html", profile=dict)


@app.route("/list")
def get_list_elements():
    url = "https://rickandmortyapi.com/api/character"
    response = urllib.request.urlopen(url)
    characters = response.read()
    dict = json.loads(characters)

    characters = []

    for character in dict["results"]:
        character = {"name": character["name"], "status": character["status"]}
        characters.append(character)

    return {"characters": characters}


@app.route("/locations")
def get_locations():
    url = "https://rickandmortyapi.com/api/location"
    response = urllib.request.urlopen(url)
    location = response.read()
    dict = json.loads(location)

    locations = []

    for location in dict["results"]:
        location = {
            "id": location["id"],
            "name": location["name"],
            "type": location["type"],
            "dimension": location["dimension"],
        }

        locations.append(location)

    return render_template("locations.html", locations=locations)


# @app.route("/locations/<id>")
# def get_locations_id(id):
#     url = "https://rickandmortyapi.com/api/location/" + id
#     response = urllib.request.urlopen(url)
#     location = response.read()
#     dict = json.loads(location)

#     locations = []

#     for location in dict["results"]:
#         location = {
#             "id": location["id"],
#             "name": location["name"],
#             "type": location["type"],
#             "dimension": location["dimension"],
#         }

#         locations.append(location)

#     return render_template("location.html", locations=locations)


@app.route("/episodes")
def get_episodes():
    url = "https://rickandmortyapi.com/api/episode/"
    response = urllib.request.urlopen(url)
    episode = response.read()
    dict = json.loads(episode)

    episodes = []

    for episode in dict["results"]:
        episode = {
            "id": episode["id"],
            "name": episode["name"],
            "air_date": episode["air_date"],
            "episode": episode["episode"],
        }

        episodes.append(episode)

    return render_template("episodes.html", episodes=episodes)


if __name__ == "__main__":
    app.run(debug=True)
