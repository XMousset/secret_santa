import json

CONFIG_NAME = "config.json"


def load_config(json_name):
    """Load the json data.

    Parameters
    ----------
    json_name : str
        Name of the json file (must contain '.json').

    Returns
    -------
    dict
        A dict with the config informations.
    """
    with open(json_name, "r", encoding="utf-8") as file:
        json_dict = json.load(file)
    return json_dict


CONFIG = load_config(CONFIG_NAME)