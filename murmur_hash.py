"""MurmurHash implementation with dataset loading and collision analysis."""

from typing import List, Dict
import json
import os
import time


def murmurhash(key: str, seed: int = 0) -> int:
    """Compute the MurmurHash for a given string."""
    key_bytes = key.encode('utf-8')
    length = len(key_bytes)
    h = seed
    c1 = 0xcc9e2d51
    c2 = 0x1b873593
    r1 = 15
    r2 = 13
    m = 5
    n = 0xe6546b64

    # Process the input in 4-byte chunks
    for i in range(0, length // 4):
        k = int.from_bytes(key_bytes[i * 4:(i + 1) * 4], byteorder='little')
        k = (k * c1) & 0xFFFFFFFF
        k = (k << r1 | k >> (32 - r1)) & 0xFFFFFFFF
        k = (k * c2) & 0xFFFFFFFF

        h ^= k
        h = (h << r2 | h >> (32 - r2)) & 0xFFFFFFFF
        h = (h * m + n) & 0xFFFFFFFF

    # Process the remaining bytes
    remaining_bytes = length & 3
    if remaining_bytes:
        k = int.from_bytes(key_bytes[-remaining_bytes:], byteorder='little')
        k = (k * c1) & 0xFFFFFFFF
        k = (k << r1 | k >> (32 - r1)) & 0xFFFFFFFF
        k = (k * c2) & 0xFFFFFFFF
        h ^= k

    # Finalize the hash
    h ^= length
    h ^= (h >> 16)
    h = (h * 0x85ebca6b) & 0xFFFFFFFF
    h ^= (h >> 13)
    h = (h * 0xc2b2ae35) & 0xFFFFFFFF
    h ^= (h >> 16)

    return h


def process_dataset(file_path: str, seed: int = 0):
    """
    Load a dataset from a file, hash its keys using MurmurHash, and calculate collision statistics.
    :param file_path: Path to the dataset file.
    :param seed: Seed value for the MurmurHash function.
    """
    with open(file_path, 'r') as f:
        dataset = json.load(f)

    print(f"\nProcessing dataset: {file_path}")

    # Start timing
    start_time = time.time()

    # Hash the dataset using MurmurHash
    hashed_data: Dict[int, List[str]] = {}
    for key, value in dataset.items():
        h = murmurhash(key, seed)  # Compute the MurmurHash
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
        process_dataset(dataset_path, seed=42)
