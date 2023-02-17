# import json
# import importlib.resources
# from typing import Dict
#
#
# default_chip = """
# {
#     "type" : "Default"
# }
# """
#
#
# def load_all() -> Dict[str, Dict]:
#     chip_data = {"Default": json.loads(default_chip)}
#     return chip_data


# try:
#     with importlib.resources.open_text('biautom.chipdata', 'gkass.json') as file:
#         grass_content = json.load(file)
# except:
#     grass_content = json.loads(default_chip)
