# Analyze Purchases CLI

## Overview

This Python CLI application processes purchase data from a JSON file, computes various statistics, and outputs the results in JSON format. The application is modularized, tested, and can be run in a Docker container.

## Features

- Calculates the following statistics:
  - Total volume of spend
  - Average purchase value
  - Maximum purchase value
  - Median purchase value
  - Number of unique products purchased
- Supports JSON input for purchase data.
- Outputs results in JSON format.
- Can be run as a Docker container for consistent environment setup.
- Includes a suite of unit tests for reliability.

## Assumptions

- Each purchase in the JSON input contains `product_name`, `quantity`, and `price`.
- `quantity` is assumed to be a positive integer.
- `price` is assumed to be a non-negative float or integer.
- The input JSON file follows a predefined structure:
  ```json
   [
    {
        "brand": "newventure.co", 
        "customer_id": "a45f2398-3f57-4d83-84bf-87afc31b483a", 
        "items": [
            {
                "department": "Tools", 
                "price": "249.00", 
                "product_category": "Sausages", 
                "product_name": "Intelligent Fresh Pizza", 
                "quantity": 1
            }, 
            {
                "department": "Health", 
                "price": "366.00", 
                "product_category": "Mouse", 
                "product_name": "Refined Wooden Hat", 
                "quantity": 2
            }
        ], 
        "purchase_id": "3655582c-4b0c-4db4-9b53-b2e0d06bba8d"
    }, 
    {
        "brand": "Hammerbarn", 
        "customer_id": "df23cfd4-d200-4f02-962d-78a9e6031f24", 
        "items": [
            {
                "department": "Outdoors", 
                "price": "549.00", 
                "product_category": "Computer", 
                "product_name": "Licensed Soft Table", 
                "quantity": 2
            }, 
            {
                "department": "Electronics", 
                "price": "330.00", 
                "product_category": "Cheese", 
                "product_name": "Rustic Cotton Pizza", 
                "quantity": 1
            }
        ], 
        "purchase_id": "3731f03f-f7ac-4089-b43d-13d3845b67e0"
    },
  ...
  ]
  ```
- The JSON file is well-formed and can be parsed by the standard `json` library.

## Considerations

- **Error Handling:** The application does not currently handle errors related to malformed JSON input, invalid data types, or missing fields. Ensure that the input data adheres to the expected format.
- **Scalability:** The current implementation assumes that the entire dataset can fit into memory. For large datasets, consider using a more memory-efficient approach or processing the data in chunks.
- **Performance:** The application is designed for simplicity and readability. For performance-critical applications, consider optimizing the calculation logic or using specialized libraries.

## Installation

### Requirements

- Python 3.11 or higher
- `pip` (Python package installer)
- Docker (for running the application in a container)

### Installation Steps

1. **Clone the repository:**

    ```bash
    git clone https://github.com/kk-858/analyze-purchases-cli.git
    cd analyze-purchases-cli
    ```

2. **Install dependencies to run the cli app:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Run tests (optional):**

    To ensure everything is set up correctly, you can run the unit tests:

    ```bash
    pip install -r requirement.txt
    python -m unittest discover -s tests
    ```

## Usage

### Running the CLI

To analyze a purchases JSON file, use the following command:

```bash
python -m analyze_purchases.cli /path/to/purchases.json
```

Example output:

```json
{
    "total_volume_spend": 1500.0,
    "average_purchase_value": 300.0,
    "maximum_purchase_value": 600.0,
    "median_purchase_value": 300.0,
    "number_of_unique_products_purchased": 5
}
```

### Docker Usage

If you prefer to run the application in a Docker container:

1. **Build the Docker image:**

    ```bash
    docker build -t analyze-purchases-cli .
    ```

2. **Run the Docker container:**

    ```bash
    docker run --rm -v /path/to/your/json/files:/data analyze-purchases-cli /data/file_name.json
    ```
   1. *Run the Docker container with sample input:*
    ```bash
   docker run --rm analyze-purchases-cli /app/sample-input/purchases_v1.json
    ```

### Running Tests

To run the unit tests using `unittest`:

```bash
python -m unittest discover -s tests
```

Or with `pytest` (if installed):

```bash
pytest tests/
```

Running tests with Docker
1. Build the docker image
    ```bash
    docker build -f Dockerfile.test -t analyze-purchases-cli-test .
    ```
2. Run the docker container
    ```bash
    docker run --rm analyze-purchases-cli-test
    ```

## Project Structure

```
analyze_purchases/
│
├── analyze_purchases/
│   ├── __init__.py
│   ├── cli.py
│   ├── calculations.py
│   └── utils.py
│
├── tests/
│   ├── __init__.py
│   ├── test_calculations.py
│   ├── test_utils.py
│   └── test_cli.py
│
├── Dockerfile
├── Dockerfile.test
├── requirements.txt
└── requirements-dev.txt
```

## Future Enhancements

- Improve performance for large datasets.
- Support additional input/output formats (e.g., CSV, XML).
- Provide detailed logging and debugging information.