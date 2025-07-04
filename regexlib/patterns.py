import re

USCAN_PHONE_REGEX = re.compile(
    r'(?:\+1[-.\s]?)?(?:\(?\d{3}\)?[-.\s]?){1}\d{3}[-.\s]?\d{4}'
)

INTER_PHONE_REGEX = re.compile(
    r'\+[0-9\s\-\(\).]{7,20}'
)

SSN_REGEX = re.compile(
    r'\d{3}-\d{2}-\d{4}|\d{3}\s*\d{3}\s*\d{3}'
)

DOB_REGEX = re.compile(
    r'\d{1,2}[/-]\d{1,2}[/-]\d{2,4}|\d{2,4}[/-]\d{1,2}[/-]\d{1,2}'
)

IP_REGEX = re.compile(
    r'\d{1,3}(?:\.\d{1,3}){3}'
)

CC_REGEX = re.compile(
    r'\s*\d{16}\s*'
)

DL_REGEX = re.compile(
    r'[A-Z]{0,3}[0-9]+',
    re.IGNORECASE
)

EMAIL_REGEX = re.compile(
    r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
)
