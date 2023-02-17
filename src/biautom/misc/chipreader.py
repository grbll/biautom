import json
import re
import importlib.resources
from typing import Dict


default_chip = """
{
    "type" : "Default"
}
"""


def load_all() -> Dict[str, Dict]:
    file_list = [file for file in importlib.resources.contents('biautom.chipdata') if re.match('[A-z]*\.json', file)]
    chip_data = {"default": json.loads(default_chip)}

    for file in file_list:
        chip_data.update({file.split('.')[0] : json.load(importlib.resources.open_text('biautom.chipdata', file))})
    
    return chip_data

print(load_all())
