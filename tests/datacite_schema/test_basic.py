import requests
from datacite_schema.schema4.pkg_4.metadata import Resource
import json


def test_resource(data_folder):
    d = json.loads((data_folder / "example.json").read_text())
    print(json.dumps(d, indent=4))
    Resource(
        **json.loads((data_folder / "example.json").read_text())["data"]["attributes"]
    )