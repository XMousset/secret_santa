import csv
import json


class ChristmasFriend:
    """A class to represent a friend and manage its informations."""

    def __init__(self, **kwargs):
        self.name = kwargs["Name"]
        self.mail = kwargs["Email"]
        self.exclusions = kwargs["Exclusions"].split(" ")
        self.exclusions.append(self.name)
        self.gifts_ideas = kwargs.get("Gifts ideas", "")
    def __repr__(self):
        return self.name

    def __eq__(self, friend):
        if not isinstance(friend, ChristmasFriend):
            raise ValueError("'friend' must be a ChristmasFriend object.")
        return self.name == friend.name
    
    def is_excluded_for(self, friend):
        if not isinstance(friend, ChristmasFriend):
            raise ValueError("'friend' must be a ChristmasFriend object.")
        lower_excl = [excl.lower().strip(",") for excl in friend.exclusions]
        return self.name.lower() in lower_excl


def load_config(json_name):
    """Load the file 'config.json'.

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


def tsv2friends(tsv_name):
    """Get all friends from tsv file.

    Parameters
    ----------
    tsv_name : str
        The name of the tsv file containing the friends informations.
        Must contain '.tsv'.

    Returns
    -------
    list of ChristmasFriend
        A list containing ChristmasFriend objects.
    """
    with open(tsv_name, mode= "r", encoding="utf-8") as tsvfile:
        data_friends = list(csv.DictReader(tsvfile, delimiter="\t"))
        friends_list = []
        for data in data_friends:
            friends_list.append(ChristmasFriend(**data))
        return friends_list
