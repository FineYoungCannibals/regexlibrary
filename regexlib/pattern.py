import re

class RegexPattern:
    def __init__(self, pattern: str, description: str, author: str = "BlackMesaRF", flags=0):
        self.pattern = re.compile(pattern, flags)
        self.description = description
        self.author = author

    def match(self, text):
        return self.pattern.match(text)

    def search(self, text):
        return self.pattern.search(text)

    def findall(self, text):
        return self.pattern.findall(text)

    def __repr__(self):
        return f"<RegexPattern: {self.description}>"
