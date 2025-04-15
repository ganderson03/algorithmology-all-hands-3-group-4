import json
import os
import struct


def custom_64bit_hash(key):
    """
    A simple custom 64-bit hash function to simulate CityHash64.
    :param key: The input string to hash.
    :return: A 64-bit integer hash.
    """
    # Convert the key to bytes
    key_bytes = key.encode('utf-8')

    # Initialize a 64-bit hash value
    hash_value = 0x123456789ABCDEF0

    # Process each byte in the key
    for byte in key_bytes:
        hash_value ^= byte
        hash_value = (hash_value * 0x100000001B3) & 0xFFFFFFFFFFFFFFFF  # Keep it 64-bit

    return hash_value


def process_dataset(file_path):
    """
    Load a dataset from a file, hash its keys using a custom 64-bit hash function,
    and calculate collision statistics.
    :param file_path: Path to the dataset file.
    """
    with open(file_path, 'r') as f:
        dataset = json.load(f)

    print(f"\nProcessing dataset: {file_path}")

    # Inline implementation of hashing with the custom hash function
    hashed_data = {}
    for key, value in dataset.items():
        h = custom_64bit_hash(key)  # Use the custom 64-bit hash function
        if h in hashed_data:
            hashed_data[h].append((key, value))  # Handle collisions
        else:
            hashed_data[h] = [(key, value)]

    # Calculate collision statistics
    total_collisions = sum(1 for v in hashed_data.values() if len(v) > 1)
    total_keys = len(dataset)
    unique_hashes = len(hashed_data)

    print(f"Total keys: {total_keys}")
    print(f"Unique hash values: {unique_hashes}")
    print(f"Total collisions: {total_collisions}")

    # Display a few collisions if they exist
    if total_collisions > 0:
        print("\nSample collisions:")
        for hval, items in hashed_data.items():
            if len(items) > 1:
                print(f"Hash: {hval} -> Items: {items}")
                break  # Display only the first collision


if __name__ == "__main__":
    # Directory containing the datasets
    dataset_dir = "datasets"

    # Process each dataset
    for dataset_file in ["dataset_5k.json", "dataset_10k.json", "dataset_20k.json"]:
        file_path = os.path.join(dataset_dir, dataset_file)
        if os.path.exists(file_path):
            process_dataset(file_path)
        else:
            print(f"Dataset file not found: {file_path}")