import json

def load_relationships():

    with open("schema/relationships.json") as f:
        return json.load(f)