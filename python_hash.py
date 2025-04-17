import json
import os


def store_with_builtin_hash(data):
    """
    Store items in a dictionary using Python's built-in hash() to simulate
    hashing behavior and observe collisions and performance.
    """
    storage = {}
    for item in data:
        h = hash(item)
        if h in storage:
            storage[h].append(item)  # Potential collision
        else:
            storage[h] = [item]
    return storage


def process_dataset(file_path):
    """
    Load a dataset from a file, hash its keys using Python's built-in hash function,
    and calculate collision statistics.
    :param file_path: Path to the dataset file.
    """
    with open(file_path, "r") as f:
        dataset = json.load(f)

    print(f"\nProcessing dataset: {file_path}")

    # Hash the dataset using the built-in hash function
    hashed_data = store_with_builtin_hash(dataset)

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
