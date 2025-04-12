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


# to have an idea about the main and how to use the function:

if __name__ == "__main__":
    keys = ["apple", "banana", "orange", "apple", "grape", "banana"]
    hashed_data = store_with_builtin_hash(keys)

    print("=== Hash Table ===")
    for hval, items in hashed_data.items():
        print(f"Hash: {hval} -> Items: {items}")

    collisions = {k: v for k, v in hashed_data.items() if len(v) > 1}
    print("\n=== Collisions ===")
    for hval, items in collisions.items():
        print(f"Hash: {hval} -> {items}")

    # Summary of collisions
    total_keys = len(keys)
    unique_hashes = len(hashed_data)
    total_collisions = sum(1 for v in hashed_data.values() if len(v) > 1)

    print("\n=== Collision Summary ===")
    print(f"Total keys: {total_keys}")
    print(f"Unique hash values: {unique_hashes}")
    print(f"Total collisions: {total_collisions}")

print("\nNote: For consistent hash values across runs, set the environment variable:")
print("PYTHONHASHSEED=0 python your_script.py")

# You can measure collisions by checking where the value list has more than one item:
# collisions = {k: v for k, v in hashed_data.items() if len(v) > 1}
# print("Collisions:", collisions)
