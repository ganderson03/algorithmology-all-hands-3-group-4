import json
import os
from collections import defaultdict, Counter
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


# def plot_bucket_histogram(hash_buckets: defaultdict, title: str):
#     """Plot a histogram showing how many buckets had 1, 2, 3... keys."""
#     bucket_sizes = [len(v) for v in hash_buckets.values()]
#     size_distribution = Counter(bucket_sizes)

#     sizes = sorted(size_distribution.keys())
#     counts = [size_distribution[size] for size in sizes]

#     plt.figure(figsize=(10, 6))
#     plt.bar(sizes, counts, width=0.6, edgecolor='black')
#     plt.xlabel("Number of Keys in Bucket")
#     plt.ylabel("Number of Buckets")
#     plt.title(f"Hash Bucket Size Distribution: {title}")
#     plt.xticks(sizes)
#     plt.grid(axis='y', linestyle='--', alpha=0.7)
#     plt.tight_layout()
#     plt.show()


def calculate_collisions(dataset: Dict[str, str], title: str = "") -> int:
    """Hash keys and count collisions. Plot histogram."""
    hash_buckets = defaultdict(list)

    for key in dataset.keys():
        h = djb2(key)
        hash_buckets[h].append(key)

    total_collisions = sum(1 for v in hash_buckets.values() if len(v) > 1)
    total_colliding_keys = sum(len(v) - 1 for v in hash_buckets.values() if len(v) > 1)

    print(f"  Distinct hash values: {len(hash_buckets)}")
    print(f"  Total collisions (buckets with >1 key): {total_collisions}")
    print(f"  Total colliding keys (extra keys in collision buckets): {total_colliding_keys}")

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
