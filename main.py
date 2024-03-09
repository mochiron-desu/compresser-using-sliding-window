import random
from collections import defaultdict
import bisect

# Function to generate a random array
def randArrGen(length, minimum=0, maximum=10):
    arr = []
    for _ in range(length):
        arr.append(random.randint(minimum, maximum))
    return arr

# Function to create unique sets of fixed window size from an array
def createSets(arr, window_size):
    unique_sets = set()
    for i in range(len(arr) - window_size + 1):
        window = tuple(arr[i:i + window_size])
        if window not in unique_sets:
            unique_sets.add(window)
            yield window

# Function to create a mapping from unique sets to integers
def createMapping(unique_sets):
    directory = defaultdict(lambda: len(directory) + 1)
    for t in unique_sets:
        directory[t]
    return directory

# Function to compress an array using the mapping
def compress(arr, directory, window_size):
    return [directory[tuple(arr[i:i + window_size])] for i in range(len(arr) - window_size + 1)]

# Function to decompress a compressed array using the mapping
def decompress(compressedArr, directory, window_size):
    result = []
    dirKeyList = list(directory.keys())
    dirValList = sorted(directory.values())

    for i in compressedArr:
        idx = bisect.bisect_left(dirValList, i)
        key = dirKeyList[idx]
        if not result:
            result.extend(key)
        else:
            result.append(key[-1])

    return result

if __name__ == '__main__':
    for i in range(0, 20):
        # Generate a random array
        arr = randArrGen(random.choice(range(10, 1000)))
        window_size = random.choice(range(1, 10))

        # Create unique sets from the array
        unique_sets = list(createSets(arr, window_size))

        # Create a mapping from unique sets to integers
        directory = createMapping(unique_sets)

        # Compress the array
        compressedArr = compress(arr, directory, window_size)

        # Decompress the compressed array
        decompressedArr = decompress(compressedArr, directory, window_size)

        # Check if decompressed array matches the original array
        if arr == decompressedArr:
            print("Successfully decompressed")
        else:
            print("ERROR")
        print(f"ARR SIZE: {len(arr)}")
        print(f"WINDOW SIZE: {window_size}")