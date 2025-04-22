import json
import os
import time  # Import the time module


def simple_modulo_hash(key, modulo=1000):
    """
    A simple hash function that calculates the sum of the ASCII values of the characters
    in the key and takes the modulo of the result.
    :param key: The input string to hash.
    :param modulo: The modulo value to limit the hash range.
    :return: An integer hash value.
    """
    # Calculate the sum of ASCII values of the characters in the key
    ascii_sum = sum(ord(char) for char in key)
    # Return the hash value as the modulo of the sum
    return ascii_sum % modulo


def process_dataset(file_path, modulo=1000):
    """
    Load a dataset from a file, hash its keys using a simple modulo-based hash function,
    and calculate collision statistics.
    :param file_path: Path to the dataset file.
    :param modulo: The modulo value to limit the hash range.
    """
    with open(file_path, 'r') as f:
        dataset = json.load(f)

    print(f"\nProcessing dataset: {file_path}")

    # Start timing
    start_time = time.time()

    # Inline implementation of hashing with the simple modulo-based hash function
    hashed_data = {}
    for key, value in dataset.items():
        h = simple_modulo_hash(key, modulo)  # Use the simple modulo-based hash function
        if h in hashed_data:
            hashed_data[h].append((key, value))  # Handle collisions
        else:
            hashed_data[h] = [(key, value)]

    # Stop timing
    end_time = time.time()
    elapsed_time = end_time - start_time

    # Calculate collision statistics
    total_collisions = sum(1 for v in hashed_data.values() if len(v) > 1)
    total_keys = len(dataset)
    unique_hashes = len(hashed_data)

    print(f"Total keys: {total_keys}")
    print(f"Unique hash values: {unique_hashes}")
    print(f"Total collisions: {total_collisions}")
    print(f"Time taken to hash dataset: {elapsed_time:.4f} seconds")

    # Display a few collisions if they exist
    if total_collisions > 0:
        print("\nSample collisions:")
        for hval, items in hashed_data.items():
            if len(items) > 1:
                print(f"Hash: {hval} -> Items: {items}")
                break  # Display only the first collision


if __name__ == "__main__":
    # Directory containing the datasets
    datasets_dir = os.path.join(os.path.dirname(__file__), "datasets")

    # List all dataset files in the directory
    dataset_files = [f for f in os.listdir(datasets_dir) if f.endswith(".json")]

    # Process each dataset file
    for dataset_file in dataset_files:
        dataset_path = os.path.join(datasets_dir, dataset_file)
        process_dataset(dataset_path, modulo=1000)