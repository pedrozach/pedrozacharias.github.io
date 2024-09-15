# pedrozacharias.github.io
Data Engineer (Python &amp; SQL) Portfolio

## Project Structure

    data_product_validator/
    ├── main.py
    ├── schemas/
    │   ├── v1/
    │   │   └── data_product_specification.cue
    │   └── v2/
    │       └── data_product_specification.cue
    ├── sample_data_product.yaml
    ├── Pipfile
    ├── Pipfile.lock
    └── README.md

## Instructions

1. **Install `pipenv` if you haven't already:**
    ```sh
    pip install pipenv
    ```

2. **Create a `Pipfile` and install dependencies:**
    ```sh
    pipenv install
    ```

3. **Activate the virtual environment:**
    ```sh
    pipenv shell
    ```

4. **Run the validation script:**
    ```sh
    python main.py
    ```

5. **Versioning:**
   - To use a specific version of the schema, update the `schema_file_path` in `main.py` to point to the desired version.
   - Example: `schema_file_path = 'schemas/v1/data_product_specification.cue'`