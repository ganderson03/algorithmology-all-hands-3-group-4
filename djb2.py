import json
import os
from collections import defaultdict, Counter
import time  # Import the time module
from typing import Dict
# import matplotlib.pyplot as plt


def djb2(key: str) -> int:
    """Hash function: DJB2 with 12-bit truncation for collision analysis."""
    h = 5381
    for c in key:
        h = ((h << 5) + h) + ord(c)  # h * 33 + ord(c)
    return h & 0xFFFF  # 12-bit hash space (4096 buckets)


def load_json_dataset(file_path: str) -> Dict[str, str]:
    """Load a JSON file as a dictionary."""
    with open(file_path, 'r', encoding='utf-8') as f:
        dataset = json.load(f)
    print(f"\nProcessing dataset: {file_path}")
    return dataset

def calculate_collisions(dataset: Dict[str, str], title: str = "") -> int:
    """Hash keys and count collisions. Plot histogram."""
    start_time = time.time()
    hash_buckets = defaultdict(list)

    for key in dataset.keys():
        h = djb2(key)
        hash_buckets[h].append(key)

    total_collisions = sum(1 for v in hash_buckets.values() if len(v) > 1)
    total_colliding_keys = sum(len(v) - 1 for v in hash_buckets.values() if len(v) > 1)

    # Stop timing
    end_time = time.time()
    elapsed_time = end_time - start_time

    print(f"Total keys: {len(dataset)}")
    print(f"  Distinct hash values: {len(hash_buckets)}")
    print(f"  Total collisions (buckets with >1 key): {total_collisions}")
    print(f"  Total colliding keys (extra keys in collision buckets): {total_colliding_keys}")
    print(f"Time taken to hash dataset: {elapsed_time:.4f} seconds")

    # plot_bucket_histogram(hash_buckets, title)

    return total_colliding_keys


if __name__ == "__main__":
    # Directory containing the datasets
    datasets_dir = os.path.join(os.path.dirname(__file__), "datasets")

    # List all JSON dataset files
    dataset_files = [f for f in os.listdir(datasets_dir) if f.endswith(".json")]

    # Process each dataset
    for dataset_file in sorted(dataset_files):
        dataset_path = os.path.join(datasets_dir, dataset_file)
        dataset = load_json_dataset(dataset_path)
        calculate_collisions(dataset, title=dataset_file)
