import json
from jsonschema import validate, ValidationError

def load_frx(path, schema_path="frx_schema.json"):
    """Load and validate an FRX or JSON alter file."""

    # Load the schema file
    try:
        with open(schema_path, "r", encoding="utf-8") as f:
            schema = json.load(f)
    except FileNotFoundError:
        print("❌ Schema file not found! Make sure 'frx_schema.json' is in the same directory.")
        return None

    # Load the alter file (regardless of extension)
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"❌ File not found: {path}")
        return None
    except json.JSONDecodeError as e:
        print(f"❌ Invalid JSON syntax in {path}: {e}")
        return None

    # Validate the alter file against the schema
    try:
        validate(instance=data, schema=schema)
        print(f"✅ {path} passed validation!")
    except ValidationError as e:
        print(f"❌ Validation error: {e.message}")
        return None

    return data


def display_basic_info(data):
    """Print a summary of basic alter details."""
    basic = data.get("basic", {})
    meta = data.get("meta", {})
    system = data.get("system", {})

    print("\n=== ALTER DETAILS ===")
    print(f"Name: {basic.get('name', 'Unnamed')}")
    if basic.get("gender"):
        print(f"Genders: {', '.join(basic.get('gender'))}")
    if basic.get("color"):
        print(f"Color: {basic.get('color')}")
    print(f"ID: {meta.get('id', 'N/A')}")
    status = meta.get("status", {})
    print(f"Currently Active: {status.get('isactive', False)}")

    if "relationships" in system:
        print("\nRelationships:")
        for name, rel in system["relationships"].items():
            print(f" - {name}: {rel.get('relationship', 'unspecified')}")


if __name__ == "__main__":
    # Interactive prompt
    print("🔹 FRX Alter Loader 🔹")
    path = input("Enter the path to the alter file (.frx or .json): ").strip()

    alter = load_frx(path)
    if alter:
        display_basic_info(alter)