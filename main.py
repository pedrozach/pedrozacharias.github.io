import yaml
import os
import json
from jsonschema import validate, ValidationError

def validate_with_jsonschema(yaml_data_str, json_schema_file):
    yaml_data = yaml.safe_load(yaml_data_str)
    with open(json_schema_file, 'r') as file:
        json_schema = json.load(file)
    try:
        validate(instance=yaml_data, schema=json_schema)
        print("JSON Schema validation successful.")
        return True
    except ValidationError as e:
        print("JSON Schema validation failed:")
        print(e)
        return False

# Example usage
if __name__ == "__main__":
    # Read the YAML data from a file
    with open('example.yaml', 'r') as file:
        yaml_data_str = file.read()

    # Specify the path to your schema files
    json_schema_file = 'schemas/v1/data_product_specification.json'

    # Validate the YAML data against the JSON schema
    validate_with_jsonschema(yaml_data_str, json_schema_file)
