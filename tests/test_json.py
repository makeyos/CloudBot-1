"""
Travis Test file:
Test JSON files for errors.
"""

import json
from collections import OrderedDict
from pathlib import Path

import pytest


def get_files():
    dirs = ("cloudbot", "data", "tests", "travis", "docs")
    return [
        file
        for file in Path().rglob("*.json")
        if len(file.parts) == 1 or file.parts[0] in dirs
    ]


@pytest.mark.parametrize("json_file", get_files())
def test_json(json_file):
    with json_file.open(encoding="utf-8") as f:
        text = f.read()

    data = json.loads(text, object_pairs_hook=OrderedDict)
    formatted_text = json.dumps(data, indent=4) + "\n"
    assert formatted_text == text, "Improperly formatted JSON file"
