import re

USCAN_PHONE_REGEX = {
    "pattern": re.compile(
        r'(?:\+1[-.\s]?)?(?:\(?\d{3}\)?[-.\s]?){1}\d{3}[-.\s]?\d{4}'
    ),
    "description": "Matches US and Canadian phone numbers, with optional country code, parentheses, spaces, dashes, or dots."
}
INTER_PHONE_REGEX = {
    "pattern": re.compile(
        r'\+[0-9\s\-\(\).]{7,20}'
    ),
    "description": "Matches international phone numbers with country code, allowing spaces, dashes, parentheses, and dots."
}

SSN_REGEX = {
    "pattern": re.compile(
        r'\d{3}-\d{2}-\d{4}|\d{3}\s*\d{3}\s*\d{3}'
    ),
    "description": "Matches US Social Security Numbers (SSN) in standard or space-separated formats."
}

DOB_REGEX = {
    "pattern": re.compile(
        r'\d{1,2}[/-]\d{1,2}[/-]\d{2,4}|\d{2,4}[/-]\d{1,2}[/-]\d{1,2}'
    ),
    "description": "Matches dates of birth in MM/DD/YYYY, DD/MM/YYYY, or YYYY/MM/DD formats with slashes or dashes."
}

IP_REGEX = {
    "pattern": re.compile(
        r'\d{1,3}(?:\.\d{1,3}){3}'
    ),
    "description": "Matches IPv4 addresses."
}

CC_REGEX = {
    "pattern": re.compile(
        r'\s*\d{16}\s*'
    ),
    "description": "Matches 16-digit credit card numbers, allowing optional surrounding whitespace."
}

DL_REGEX = {
    "pattern": re.compile(
        r'[A-Z]{0,3}[0-9]+',
        re.IGNORECASE
    ),
    "description": "Matches driver's license numbers with up to 3 letters followed by digits (case-insensitive)."
}

NAME_REGEX = {
    "pattern": re.compile(
        r"[A-ZÀ-ÖØ-öø-ÿ'’\-\. ]{2,}(?: [A-ZÀ-ÖØ-öø-ÿ'’\-\. ]{2,})+",
        re.IGNORECASE
    ),
    "description": "Matches international human names, allowing letters (including accented), apostrophes, hyphens, periods, and spaces."
}

EMAIL_REGEX = {
    "pattern": re.compile(
        r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
    ),
    "description": "Matches email addresses."
}
