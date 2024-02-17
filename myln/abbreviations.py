class Abbreviations:
    default_abbreviations = {
        "as soon as possible": "ASAP",
        "for your information": "FYI",
        "and": "&",
        "appointment": "appt",
        "approximately": "approx",
        "department": "dept",
        "hello": "hi",
        "information": "info",
        "introduction": "intro",
        "number": "#",
        "percent": "%",
        "question": "Q",
        "answer": "A",
        "reference": "ref",
        "without": "w/o",
        "with": "w/",
        "example": "e.g.",
        "that is": "i.e.",
        "please": "pls",
        "thanks": "thx",
        "thank you": "ty",
        "application": "app",
        "technology": "tech",
        "university": "univ",
        "versus": "vs",
        "estimate": "est",
        "demonstration": "demo",
        "government": "govt"
    }

    @classmethod
    def apply_abbreviations(cls, text):
        for phrase, abbreviation in cls.default_abbreviations.items():
            text = text.replace(phrase, abbreviation)
        return text
