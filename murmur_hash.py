"""MurmurHash implementation with dataset loading."""

from typing import List


def murmurhash(key: str, seed: int = 0) -> int:
    """Compute the MurmurHash for a given string.
    """
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


def load_dataset(file_path: str) -> List[str]:
    """Load a dataset from a file, where each line is treated as a separate entry."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return [line.strip() for line in file]


def hash_dataset(file_path: str, seed: int = 0) -> List[int]:
    """Hash each line of a dataset using MurmurHash."""
    dataset = load_dataset(file_path)
    return [murmurhash(line, seed) for line in dataset]


if __name__ == "__main__":
    # Example usage
    dataset_file = "dataset.txt"  # Replace with the path to your dataset file
    seed_value = 42

    try:
        hashes = hash_dataset(dataset_file, seed_value)
        for i, h in enumerate(hashes, start=1):
            print(f"Line {i}: Hash = {h}")
    except FileNotFoundError:
        print(f"Error: The file '{dataset_file}' was not found.")