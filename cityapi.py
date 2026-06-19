from fastapi import FastAPI

# start api en mode api:
# fastapi dev cityapi.py
app = FastAPI()

# simulation de db
data_villes = [
    {'nom': 'Marseille', 'code_postal': '13000', 'population': 886040},
    {'nom': 'Nice', 'code_postal': '06000', 'population': 357737},
    {'nom': 'Toulon', 'code_postal': '83000', 'population': 179116},
    {'nom': 'Aix-en-Provence', 'code_postal': '13100', 'population': 149695},
    {'nom': 'Avignon', 'code_postal': '84000', 'population': 92188},
    {'nom': 'Antibes', 'code_postal': '06600', 'population': 77637},
    {'nom': 'Cannes', 'code_postal': '06400', 'population': 74350},
    {'nom': 'La Seyne-sur-Mer', 'code_postal': '83500', 'population': 63732},
    {'nom': 'Fréjus', 'code_postal': '83600', 'population': 59719},
    {'nom': 'Hyères', 'code_postal': '83400', 'population': 55858}
]

@app.get("/ville")
def read_villes():
    return data_villes


@app.get("/ville/{code_postal}")
def read_ville(code_postal: str):
    return [ville for ville in data_villes if ville['code_postal'] == code_postal]
