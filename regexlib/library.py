from enum import Enum
from .pattern import RegexPattern
import re
import re
from enum import Enum
from .pattern import RegexPattern

class RegexLibrary(Enum):
    USCAN_PHONE = RegexPattern(
        r'(?:\+1[-.\s]?)?(?:\(?\d{3}\)?[-.\s]?){1}\d{3}[-.\s]?\d{4}',
        "Matches US and Canadian phone numbers, with optional country code, parentheses, spaces, dashes, or dots."
    )

    INTER_PHONE = RegexPattern(
        r'\+[0-9\s\-\(\).]{7,20}',
        "Matches international phone numbers with country code, allowing spaces, dashes, parentheses, and dots."
    )

    SSN = RegexPattern(
        r'\d{3}-\d{2}-\d{4}|\d{3}\s*\d{3}\s*\d{3}',
        "Matches US Social Security Numbers (SSN) in standard or space-separated formats."
    )

    DOB = RegexPattern(
        r'\d{1,2}[/-]\d{1,2}[/-]\d{2,4}|\d{2,4}[/-]\d{1,2}[/-]\d{1,2}',
        "Matches dates of birth in MM/DD/YYYY, DD/MM/YYYY, or YYYY/MM/DD formats with slashes or dashes."
    )

    IP = RegexPattern(
        r'\d{1,3}(?:\.\d{1,3}){3}',
        "Matches IPv4 addresses."
    )

    CC = RegexPattern(
        r'\s*\d{16}\s*',
        "Matches 16-digit credit card numbers, allowing optional surrounding whitespace."
    )

    DL = RegexPattern(
        r'[A-Z]{0,3}[0-9]+',
        "Matches driver's license numbers with up to 3 letters followed by digits (case-insensitive).",
        flags=re.IGNORECASE
    )

    NAME = RegexPattern(
        r"[A-ZÀ-ÖØ-öø-ÿ'’\-\. ]{2,}(?: [A-ZÀ-ÖØ-öø-ÿ'’\-\. ]{2,})+",
        "Matches international human names, allowing letters (including accented), apostrophes, hyphens, periods, and spaces.",
        flags=re.IGNORECASE
    )

    EMAIL = RegexPattern(
        r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+',
        "Matches email addresses."
    )
