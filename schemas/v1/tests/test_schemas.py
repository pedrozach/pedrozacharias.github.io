import json
import yaml
import pytest
from jsonschema import validate, ValidationError

# Helper function to load JSON schema
def load_schema(schema_path):
    with open(schema_path) as schema_file:
        return json.load(schema_file)

# Helper function to load YAML data
def load_yaml_data(data_path):
    with open(data_path) as data_file:
        return yaml.safe_load(data_file)

# Test cases for each schema
@pytest.mark.parametrize("schema_path, data_path", [
    ("schemas/v1/components/outputports/redshift.json", "schemas/v1/examples/redshift_output_example.yaml"),
    ("schemas/v1/components/outputports/trino.json", "schemas/v1/examples/trino_output_example.yaml"),
    ("schemas/v1/components/outputports/s3.json", "schemas/v1/examples/s3_output_example.yaml"),
    ("schemas/v1/data_product_specification.json", "example.yaml")
])
def test_schema_validation(schema_path, data_path):
    schema = load_schema(schema_path)
    data = load_yaml_data(data_path)
    
    try:
        validate(instance=data, schema=schema)
        print(f"{data_path} is valid")
    except ValidationError as e:
        pytest.fail(f"{data_path} is invalid: {e.message}")

if __name__ == "__main__":
    pytest.main()
