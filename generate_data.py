import random
import string
import json
import os


def generate_random_string(length=10):
    """Generate a random string of fixed length."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))


def generate_dataset(size, filename):
    """
    Generate a dataset of random key-value pairs and save it to a JSON file.
    :param size: Number of key-value pairs to generate.
    :param filename: Name of the file to save the dataset.
    """
    dataset = {generate_random_string(): generate_random_string() for _ in range(size)}
    with open(filename, 'w') as f:
        json.dump(dataset, f)
    print(f"Dataset with {size} entries saved to {filename}")


if __name__ == "__main__":
    # Directory to save datasets
    output_dir = "datasets"
    os.makedirs(output_dir, exist_ok=True)

    # Generate datasets of different sizes
    generate_dataset(5000, os.path.join(output_dir, "dataset_5k.json"))
    generate_dataset(10000, os.path.join(output_dir, "dataset_10k.json"))
    generate_dataset(20000, os.path.join(output_dir, "dataset_20k.json"))

    print("\nDatasets generated successfully!")
