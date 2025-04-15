import json
import os
import cityhash  # Ensure you have installed this library: pip install cityhash


def hash_with_cityhash(data):
    """
    Hash the keys of a dataset using the CityHash algorithm.
    :param data: Dictionary of key-value pairs.
    :return: Dictionary with CityHash64 hashes as keys and original keys as values.
    """
    hashed_data = {}
    for key, value in data.items():
        h = cityhash.cityhash(key)  # Compute CityHash for the key
        if h in hashed_data:
            hashed_data[h].append((key, value))  # Handle collisions
        else:
            hashed_data[h] = [(key, value)]
    return hashed_data


def process_dataset(file_path):
    """
    Load a dataset from a file, hash its keys using CityHash, and calculate collision statistics.
    :param file_path: Path to the dataset file.
    """
    with open(file_path, 'r') as f:
        dataset = json.load(f)

    print(f"\nProcessing dataset: {file_path}")
    hashed_data = hash_with_cityhash(dataset)

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