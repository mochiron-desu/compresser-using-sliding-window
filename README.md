# Sliding Window Array Compression in Python

This repository contains a Python implementation of array compression using sliding windows. The project aims to shorten arrays by creating unique sets of fixed window size and mapping them to integers.

## Table of Contents
- [Description](#description)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## Description

This project implements a function for compressing arrays using sliding windows. It works by:
1. Creating a set of unique subsets of a fixed window size from the array.
2. Creating a mapping from these unique subsets to integers.
3. Compressing the array using these mappings.
4. Decompressing the array back to its original form using the mapping.

## Features

- **Random Array Generation**: Generates random arrays for testing.
- **Sliding Window Subset Creation**: Creates unique subsets of a fixed window size.
- **Mapping Creation**: Maps unique subsets to integers.
- **Compression**: Compresses the array using the mapping.
- **Decompression**: Decompresses the array back to its original form.

## Installation

To use this project, simply clone the repository and navigate to the project directory:

```bash
git clone https://github.com/mochiron-desu/compresser-using-sliding-window.git
cd compresser-using-sliding-window
```

## Usage

Here is an example of how to use the functions provided in this repository:

1. **Generate a Random Array**:
    ```python
    from main import randArrGen
    arr = randArrGen(length=100, minimum=0, maximum=10)
    ```

2. **Create Unique Sets from the Array**:
    ```python
    from main import createSets
    window_size = 5
    unique_sets = list(createSets(arr, window_size))
    ```

3. **Create a Mapping from Unique Sets to Integers**:
    ```python
    from main import createMapping
    directory = createMapping(unique_sets)
    ```

4. **Compress the Array**:
    ```python
    from main import compress
    compressed_arr = compress(arr, directory, window_size)
    ```

5. **Decompress the Array**:
    ```python
    from main import decompress
    decompressed_arr = decompress(compressed_arr, directory, window_size)
    ```

6. **Check if Decompressed Array Matches Original Array**:
    ```python
    if arr == decompressed_arr:
        print("Successfully decompressed")
    else:
        print("ERROR")
    ```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
