"""CLI interface to run and time different hashing implementations."""

import os
import time
import argparse
from python_hash import process_dataset as process_builtin_hash
from modulo_hash import process_dataset as process_modulo_hash
from murmur_hash import process_dataset as process_murmur_hash
from djb2 import load_json_dataset, calculate_collisions

# Directory containing datasets
DATASET_DIR = "datasets"


def run_builtin_hash(dataset_file):
    """
    Run and time the Python built-in hash implementation on a dataset.
    """
    file_path = os.path.join(DATASET_DIR, dataset_file)
    if not os.path.exists(file_path):
        print(f"Error: Dataset file '{dataset_file}' not found in '{DATASET_DIR}'.")
        return

    print(f"Running Python built-in hash on dataset: {dataset_file}")
    start_time = time.time()
    results = process_builtin_hash(file_path)  # Capture results from the function
    end_time = time.time()
    print(f"Results: {results}")  # Automatically print results
    print(f"Time taken: {end_time - start_time:.4f} seconds")


def run_modulo_hash(dataset_file, modulo=1000):
    """
    Run and time the simple modulo-based hash implementation on a dataset.
    """
    file_path = os.path.join(DATASET_DIR, dataset_file)
    if not os.path.exists(file_path):
        print(f"Error: Dataset file '{dataset_file}' not found in '{DATASET_DIR}'.")
        return

    print(f"Running simple modulo-based hash on dataset: {dataset_file}")
    start_time = time.time()
    results = process_modulo_hash(file_path, modulo)  # Capture results from the function
    end_time = time.time()
    print(f"Results: {results}")  # Automatically print results
    print(f"Time taken: {end_time - start_time:.4f} seconds")


def run_murmur_hash(dataset_file, seed=0):
    """
    Run and time the MurmurHash implementation on a dataset.
    """
    file_path = os.path.join(DATASET_DIR, dataset_file)
    if not os.path.exists(file_path):
        print(f"Error: Dataset file '{dataset_file}' not found in '{DATASET_DIR}'.")
        return

    print(f"Running MurmurHash on dataset: {dataset_file}")
    start_time = time.time()
    process_murmur_hash(file_path, seed)  # Call the process_dataset function for MurmurHash
    end_time = time.time()
    print(f"Time taken: {end_time - start_time:.4f} seconds")


def run_djb2_hash(dataset_file):
    """
    Run and time the DJB2 hash implementation on a dataset.
    """
    file_path = os.path.join(DATASET_DIR, dataset_file)
    if not os.path.exists(file_path):
        print(f"Error: Dataset file '{dataset_file}' not found in '{DATASET_DIR}'.")
        return

    print(f"Running DJB2 hash on dataset: {dataset_file}")
    start_time = time.time()
    dataset = load_json_dataset(file_path)  # Load the dataset
    collisions = calculate_collisions(dataset, title=dataset_file)  # Calculate collisions
    end_time = time.time()
    print(f"Total collisions: {collisions}")
    print(f"Time taken: {end_time - start_time:.4f} seconds")


def main():
    # Create the argument parser
    parser = argparse.ArgumentParser(description="Run and time different hashing implementations.")
    subparsers = parser.add_subparsers(dest="command", help="Hashing implementation to run")

    # Subparser for the built-in hash command
    builtin_parser = subparsers.add_parser("builtin", help="Run Python built-in hash")
    builtin_parser.add_argument("dataset_file", help="The dataset file to process")

    # Subparser for the modulo hash command
    modulo_parser = subparsers.add_parser("modulo", help="Run simple modulo-based hash")
    modulo_parser.add_argument("dataset_file", help="The dataset file to process")
    modulo_parser.add_argument("--modulo", type=int, default=1000, help="Modulo value (default: 1000)")

    # Subparser for the MurmurHash command
    murmur_parser = subparsers.add_parser("murmur", help="Run MurmurHash")
    murmur_parser.add_argument("dataset_file", help="The dataset file to process")
    murmur_parser.add_argument("--seed", type=int, default=0, help="Seed value for MurmurHash (default: 0)")

    # Subparser for the DJB2 hash command
    djb2_parser = subparsers.add_parser("djb2", help="Run DJB2 hash")
    djb2_parser.add_argument("dataset_file", help="The dataset file to process")

    # Parse the arguments
    args = parser.parse_args()

    # Execute the appropriate function based on the command
    if args.command == "builtin":
        run_builtin_hash(args.dataset_file)
    elif args.command == "modulo":
        run_modulo_hash(args.dataset_file, args.modulo)
    elif args.command == "murmur":
        run_murmur_hash(args.dataset_file, args.seed)
    elif args.command == "djb2":
        run_djb2_hash(args.dataset_file)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
