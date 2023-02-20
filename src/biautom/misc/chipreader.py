import json
import re
import importlib.resources
from typing import Dict

from jsonschema import validate
import jsonschema

# chip_schema = {
#     "$schema": "https://json-schema.org/draft/2020-12/schema",
#     "type": "object",
#     "properties": {
#         "family": {
#             "description" : "A group of closely related chips, which may look for each other.",
#             "type": "string",
#             },
#         "category": {
#             "description": "The kingdom, the organism belongs to.",
#             "type": "string"}
#         },
#     "required": ["", "category"]
# }

default_string = """
{
    "family" : "Default",
    "category" : "*"
}
"""

chip_schema = json.load(importlib.resources.open_text("biautom.misc", "schema.json"))
default_chip = json.loads(default_string)

validate(default_chip, chip_schema)


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
