import json
import re
import importlib.resources
from typing import Dict

from jsonschema import Draft202012Validator, RefResolver


default_string = """
{
    "family" : "Default",
    "category" : "*",
    "testi" : {"test2" : "44", "test1": "hallo"}
}
"""
default_chip = json.loads(default_string)

schemas = [
    json.load(importlib.resources.open_text("biautom.misc", "chip-schema.json")),
    json.load(importlib.resources.open_text("biautom.misc", "test-schema.json")),
]

schema_store = {}

for schema in schemas:
    schema_store.update({schema["$id"] : schema})

resolver = RefResolver.from_schema(schemas[0], store=schema_store)
validator = Draft202012Validator(schemas[0], resolver=resolver)

jsonData = json.loads(default_string)
validator.validate(jsonData)


def load_all() -> Dict[str, Dict]:
    file_list = [
        file
        for file in importlib.resources.contents("biautom.chipdata")
        if re.match("[A-z]*\.json", file)
    ]
    chip_data = {"default": default_chip}

    for file in file_list:
        chip_data.update(
            {
                file.split(".")[0]: json.load(
                    importlib.resources.open_text("biautom.chipdata", file)
                )
            }
        )

    return chip_data


# print(load_all())
