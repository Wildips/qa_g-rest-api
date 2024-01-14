import json
from pathlib import Path


def load_schema(schema_cursor):
    with open(
            Path(__file__).parent.parent.joinpath(f"schemes/{schema_cursor}").absolute()
    ) as file:
        schema = json.load(file)
        return schema
