import hashlib
import json
import os

def sha256(content):
    """
    SHA-256 hash function.
    :param content: The input string to hash.
    :return: A 64-bit integer derived from SHA-256 (lower 64 bits of digest).
    """
    hash_object = hashlib.sha256(content.encode('utf-8'))
    digest = hash_object.digest()  # Full 256-bit hash (32 bytes)

    # Take the lower 8 bytes to simulate a 64-bit hash
    hash_64bit = int.from_bytes(digest[-8:], byteorder='big')
    return hash_64bit


def process_dataset(file_path):
    """
    Load a dataset from a file, hash its keys using SHA-256 (64-bit simulation),
    and calculate collision statistics.
    :param file_path: Path to the dataset file.
    """
    with open(file_path, 'r') as f:
        dataset = json.load(f)

    print(f"\nProcessing dataset: {file_path}")

    hashed_data = {}
    for key, value in dataset.items():
        h = sha256(key)
        if h in hashed_data:
            hashed_data[h].append((key, value))  # Handle collisions
        else:
            hashed_data[h] = [(key, value)]

    total_collisions = sum(1 for v in hashed_data.values() if len(v) > 1)
    total_keys = len(dataset)
    unique_hashes = len(hashed_data)

    print(f"Total keys: {total_keys}")
    print(f"Unique hash values: {unique_hashes}")
    print(f"Total collisions: {total_collisions}")

    if total_collisions > 0:
        print("\nSample collisions:")
        for hval, items in hashed_data.items():
            if len(items) > 1:
                print(f"Hash: {hval} -> Items: {items}")
                break  # Show only the first collision


if __name__ == "__main__":
    # Directory containing the datasets
    dataset_dir = "datasets"

    for dataset_file in ["dataset_5k.json", "dataset_10k.json", "dataset_20k.json"]:
        file_path = os.path.join(dataset_dir, dataset_file)
        if os.path.exists(file_path):
            process_dataset(file_path)
        else:
            print(f"Dataset file not found: {file_path}")
