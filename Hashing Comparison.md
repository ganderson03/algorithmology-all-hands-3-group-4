# Hashing Algorithm Comparison

This project provides a command-line interface to compare the performance and collision rates of several hashing algorithms when applied to JSON datasets. The following hashing algorithms are implemented and can be tested:

-   **MurmurHash:** A fast, non-cryptographic hash function suitable for general-purpose hashing.
-   **Modulo Hashing:** A simple hashing technique where the hash value is the sum of the ASCII values of the key modulo a specified number.
-   **Python Built-in Hash:** The native `hash()` function in Python.
-   **DJB2 Hashing:** A popular and relatively simple string hashing algorithm.

The program processes JSON datasets located in the `datasets` directory. These datasets are expected to be JSON files where the keys are strings to be hashed. Example datasets of 5,000, 10,000, and 20,000 entries are provided (or can be generated using `generate_data.py`).

## Project Structure

The project consists of the following Python modules:

-   `djb2.py`: Implements the DJB2 hash function and includes functionality to load JSON datasets and calculate collisions.
-   `generate_data.py`: A utility script to generate JSON datasets of specified sizes with random key-value pairs.
-   `main.py`: The main script that defines the command-line interface using `argparse` to run and time the different hashing implementations.
-   `modulo_hash.py`: Implements a simple modulo-based hash function and includes functionality to process datasets and report collision statistics.
-   `murmur_hash.py`: Implements the MurmurHash algorithm and provides a function to hash the keys of a dataset.
-   `python_hash.py`: Utilizes Python's built-in `hash()` function to process datasets and report collision statistics.
-   `datasets/`: A directory (which should be created) to store the JSON dataset files (e.g., `dataset_5k.json`, `dataset_10k.json`, `dataset_20k.json`).

## Setup

1.  **Create the `datasets` directory:**
    ```bash
    mkdir datasets
    ```

2.  **Generate datasets (optional):**
    Run the `generate_data.py` script to create sample datasets of 5,000, 10,000, and 20,000 entries.
    ```bash
    python generate_data.py
    ```
    This will create `dataset_5k.json`, `dataset_10k.json`, and `dataset_20k.json` in the `datasets` directory.

## Usage

The `main.py` script provides a command-line interface to run each hashing algorithm on a specified dataset.

```bash
python main.py <command> <dataset_file> [options]
