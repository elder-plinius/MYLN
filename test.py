from myln import Compressor

input_text = """insert-text-here
"""
try:
    compressed_text = Compressor.compress_text(input_text)
    with open('output.txt', 'w') as file:
        file.write(compressed_text)
    print("Compression successful, output saved to output.txt")
except Exception as e:
    print(f"An error occurred: {e}")
