import click
import json
from .calculations import calculate_statistics


def validate_json_structure(data) -> None:
    """
    Validate the structure of the input JSON data.
    Raises a ValueError if the validation fails.
    """
    if isinstance(data, list):
        for purchase in data:
            validate_purchase(purchase)
        return
    raise ValueError("Input data should be a JSON object.")


def validate_purchase(purchase: dict) -> None:
    """
    Validate a single purchase entry in the JSON data.
    Raises a ValueError if the validation fails.
    :type purchase: object
    """
    if not isinstance(purchase, dict):
        raise ValueError("Each purchase should be a JSON object.")

    if "purchase_id" not in purchase or not isinstance(purchase["purchase_id"], str):
        raise ValueError("Each purchase must have a 'purchase_id' as a string.")

    if "items" not in purchase:
        raise ValueError("Each purchase must have an 'items' key.")

    if not isinstance(purchase["items"], list):
        raise ValueError("'items' should be a list.")

    for item in purchase["items"]:
        validate_item(item)


def validate_item(item: dict) -> None:
    """
    Validate a single item within a purchase in the JSON data.
    Raises a ValueError if the validation fails.
    """
    if not isinstance(item, dict):
        raise ValueError("Each item should be a JSON object.")

    if "product_name" not in item or not isinstance(item["product_name"], str):
        raise ValueError("Each item must have a 'product_name' as a string.")

    if "quantity" not in item or not isinstance(item["quantity"], (int, float)):
        raise ValueError("Each item must have a 'quantity' as a number (int or float).")

    if item["quantity"] <= 0:
        raise ValueError("Quantity must be greater than zero.")

    if "price" not in item:
        raise ValueError("Each item must have a 'price'")
    try:
        float(item["price"])
    except ValueError:
        print("price should be able to cast to float")

    if float(item["price"]) <= 0:
        raise ValueError("Price per unit must be greater than zero.")


def load_and_validate_json(file_stream):
    """
    Load the JSON file and validate its structure and content.
    Returns the loaded JSON data if validation passes.
    Raises a ValueError if validation fails.
    """
    try:
        data = json.load(file_stream)
    except json.JSONDecodeError as e:
        raise ValueError(f"Failed to parse JSON: {e}")
    validate_json_structure(data)
    return data


@click.command()
@click.argument('input_file', type=click.File('r'))
def analyze_purchases(input_file) -> None:
    """
    Analyze the json file
    :param input_file:
    :return: None
    """
    json_data = list()
    try:
        json_data = load_and_validate_json(input_file)
    except ValueError as e:
        print(f"Validation error: {e}")
    results = calculate_statistics(json_data)
    print(json.dumps(results, indent=4))


if __name__ == '__main__':
    analyze_purchases()
