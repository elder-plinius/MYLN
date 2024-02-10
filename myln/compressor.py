from .abbreviations import Abbreviations

class Compressor:
    vowels = "aeiouAEIOU"

    @staticmethod
    def compress_word(word):
        """Compress a single word by removing non-initial vowels from words longer than three characters, preserving readability."""
        # Preserve words shorter than 4 characters or in uppercase (considered acronyms)
        if len(word) <= 3 or word.upper() == word:
            return word

        # Preserve the first vowel found and subsequent consonants, remove other vowels
        new_word = []
        vowel_found = False
        for char in word:
            if char in Compressor.vowels:
                if not vowel_found:
                    new_word.append(char)  # Keep the first vowel encountered
                    vowel_found = True
            else:
                new_word.append(char)  # Keep consonants
        return ''.join(new_word)

    @classmethod
    def compress_text(cls, input_text):
        """Compress a text string using abbreviations and selective vowel removal."""
        # First, apply abbreviations to the input text
        input_text = Abbreviations.apply_abbreviations(input_text)
        
        # Split text into words, compress them, and rejoin with spaces
        words = input_text.split()
        compressed_words = [cls.compress_word(word) for word in words]
        return " ".join(compressed_words)

# Example usage
if __name__ == "__main__":
    input_text = "Alice and Bob are planning to visit the university as soon as possible for your information."
    compressed_text = Compressor.compress_text(input_text)
    print("Original Text:", input_text)
    print("Compressed Text:", compressed_text)
