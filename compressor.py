import re
from string import punctuation

class MylnCompressor:
    vowels = "aeiouAEIOU"
    abbreviations = {
        "as soon as possible": "ASAP",
        "for your information": "FYI",
    }
    essential_short_words = {"with", "from", "they", "have"}

    @staticmethod
    def compress_word(word):
        if word.upper() == word or word.lower() in MylnCompressor.essential_short_words:
            return word
        
        first_vowel_index = next((i for i, char in enumerate(word) if char in MylnCompressor.vowels), None)
        
        if first_vowel_index is not None:
            compressed_word = [char for i, char in enumerate(word) if i == first_vowel_index or char not in MylnCompressor.vowels]
        else:
            compressed_word = [char for char in word]

        return ''.join(compressed_word)

    @classmethod
    def compress_text(cls, input_text):
        for phrase, abbreviation in cls.abbreviations.items():
            input_text = re.sub(r'\b' + phrase + r'\b', abbreviation, input_text, flags=re.IGNORECASE)

        words = re.findall(r'\w+|[^\w\s]', input_text, re.UNICODE)
        compressed_words = [cls.compress_word(word) if word.lower() not in cls.abbreviations.values() else word for word in words]
        return "".join(compressed_words)