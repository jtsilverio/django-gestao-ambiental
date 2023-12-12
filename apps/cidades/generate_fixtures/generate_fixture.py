import json

MODEL_NAME = "cidades.Cidades"

with open("apps/cidades/generate_fixtures/cidades_ibge.json") as data_file:
    data = json.load(data_file)

    fixtures = []
    for i, entry in enumerate(data):
        estado = entry["microrregiao"]["mesorregiao"]["UF"]["sigla"]
        cidade = entry["nome"]
        id_ibge = entry["id"]
        fixture_object = {
            "model": MODEL_NAME,
            "pk": id_ibge,
            "fields": {"nome": cidade, "estado": estado},
        }

        fixtures.append(fixture_object)

    with open("apps/cidades/fixtures/initial_data.json", "w") as fixture_file:
        fixture_file.write(json.dumps(fixtures, ensure_ascii=False))
