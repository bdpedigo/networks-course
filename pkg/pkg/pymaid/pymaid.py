import json
import logging
from pathlib import Path

import pymaid

base_path = Path(__file__).parent
try:
    file_path = (base_path / "./pymaid_credentials.json").resolve()
    with open(file_path, "r") as f:
        cred_dict = json.load(f)
    url = cred_dict["url"]
    token = cred_dict["token"]
    name = cred_dict["name"]
    pwd = cred_dict["pwd"]
    catmaid_args = (url, token, name, pwd)
except FileNotFoundError:
    msg = "Catmaid credentials not found - Pymaid functionality will be unavailable"
    raise UserWarning(msg)


def start_instance(log=False):
    if not log:
        logging.getLogger("pymaid").setLevel(logging.WARNING)
    return pymaid.CatmaidInstance(*catmaid_args)


if __name__ == "__main__":
    rm = pymaid.CatmaidInstance(*catmaid_args)
