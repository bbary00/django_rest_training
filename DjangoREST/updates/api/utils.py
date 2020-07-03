import json

def is_json(json_data):
    try:
        loaded_json = json.loads(json_data)
        is_valid = True
    except:
        is_valid = False
    return is_valid
