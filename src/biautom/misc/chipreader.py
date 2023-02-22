from importlib.abc import Traversable
import json
import re
from importlib.resources import contents, open_text
from importlib.resources import files
from importlib import import_module
from types import ModuleType
from typing import Dict

from jsonschema import Draft202012Validator, RefResolver



default_string = """
{
    "family" : "Default",
    "kingdom" : "plant",
    "placement" : [{"multiplier" : 2},
                   {"check" : { "query" : { "multiplier" : 2}, "kingdom" : "you"}}]
}
"""
default_chip = json.loads(default_string)

def get_all_json(module_files: Traversable) -> list[Dict]:
    json_list: list[Dict] = []

    for file in module_files.iterdir():
        if file.is_file() and re.match("[A-z]*\.json", file.name):
            json_list.append(json.load(file.open()))
        elif file.is_dir() and file.name!="__pycache__":
            json_list = json_list + get_all_json(module_files.joinpath(file.name))
    
    return json_list


def load_schema(module_files: Traversable, base_schema_name: str)-> Draft202012Validator:
    json_list: list[Dict] = get_all_json(module_files)
    base_schema: Dict = json.load(module_files.joinpath(base_schema_name).open())

    schema_store: Dict[str,Dict] = { schema["$id"] : schema for schema in json_list}

    resolver = RefResolver.from_schema(base_schema, store = schema_store)
    return Draft202012Validator(base_schema, resolver = resolver)

def load_all() -> Dict[str, Dict]:
    file_list = [
        file
        for file in importlib.resources.contents(chip_data_files)
        if re.match("[A-z]*\.json", file)
    ]
    chip_data = {"default": default_chip}

    for file in file_list:
        chip_data.update(
            {
                file.split(".")[0]: json.load(
                    importlib.resources.open_text(chip_data_files, file)
                )
            }
        )

    return chip_data
