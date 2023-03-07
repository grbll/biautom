import json
import re
from importlib.resources import files
from importlib.abc import Traversable
from typing import Dict
from jsonschema import Draft202012Validator, RefResolver

from biautom.game.chip_data_handler import ChipDataHandler


class ChipReader:
    data: Traversable = files("biautom.data")

    @staticmethod
    def get_all_json(module_files: Traversable) -> list[Traversable]:
        json_list: list[Traversable] = []

        for file in module_files.iterdir():
            if file.is_file() and re.match("[A-z]*\.json", file.name):
                json_list.append(file)
            elif file.is_dir() and file.name != "__pycache__":
                json_list = __class__.get_all_json(file)

        return json_list

    @staticmethod
    def load_schema(
        schema_files: list[Traversable], base_schema_file: Traversable
    ) -> Draft202012Validator:
        json_list: list[Dict] = []
        for files in schema_files:
            for json_file in __class__.get_all_json(files):
                json_list.append(json.load(json_file.open()))
        
        base_schema: Dict = json.load(base_schema_file.open())

        schema_store: Dict[str, Dict] = {
            schema["$id"]: schema for schema in json_list if "$id" in schema
        }

        resolver = RefResolver.from_schema(base_schema, store=schema_store)
        return Draft202012Validator(base_schema, resolver=resolver)

    def __init__(
        self,
        chip_paths: list[str],
        schema_paths: list[str],
        schema_base_paths: list[str],
        default_string: str,
    ) -> None:
        schema_files = [
            self.__class__.data.joinpath(schema_path)
            for schema_path in schema_paths
        ]
        schema_base_files = [
            self.__class__.data.joinpath(schema_base_path)
            for schema_base_path in schema_base_paths
        ]
        chip_files: list[Traversable] = [
            chip_file
            for chip_path in chip_paths
            for chip_file in self.__class__.get_all_json(
                self.__class__.data.joinpath(chip_path)
            )
        ]

        self.validators: list[Draft202012Validator] = []
        self.chip_data = {}
        self.default = {}
        

        for schema_base_file in schema_base_files:
            self.validators.append(
                self.__class__.load_schema(schema_files, schema_base_file)
            )
        
        self.validators[0].validate(json.loads(default_string))
        if all(
            validator.is_valid(json.loads(default_string))
            for validator in self.validators
        ):
            self.default = json.loads(
                default_string,
                object_hook=lambda sub_object: ChipDataHandler(**sub_object),
            )

        for chip_file in chip_files:
            chip_dict: Dict = json.load(chip_file.open())
            if all(validator.is_valid(chip_dict) for validator in self.validators):
                self.chip_data.update(
                    {
                        chip_file.name.split(".")[0]: json.load(
                            chip_file.open(),
                            object_hook=lambda sub_dict: ChipDataHandler(**sub_dict),
                        )
                    }
                )
