# Myln Compression Package

A simple Python package for compressing text by removing non-essential vowels and applying common abbreviations.

## Installation

Install the package using pip:

```bash
pip install myln-compression
```

## Usage

To use the text compression functionality, import the `MylnCompressor` from the package and use the `compress_text` method:

```python
from myln_compression import MylnCompressor

input_text = "This is a test message, to see how as soon as possible can be compressed."
compressed_text = MylnCompressor.compress_text(input_text)
print(compressed_text)
```

## Features

- Removes vowels from non-essential words longer than three characters.
- Applies common abbreviations to reduce text length.
- Easy integration into existing Python projects.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request on GitHub.