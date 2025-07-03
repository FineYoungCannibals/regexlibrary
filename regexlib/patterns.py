import re

# Precompiled patterns
PHONE_REGEX = re.compile(r'(\+1\s?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}')
SSN_REGEX = re.compile(r'\d{3}-\d{2}-\d{4}|\d{9}')
DOB_REGEX = re.compile(r'\b\d{1,2}[/-]\d{1,2}[/-]\d{2,4}\b')
IP_REGEX = re.compile(r'\b\d{1,3}(\.\d{1,3}){3}\b')
CC_REGEX = re.compile(r'\s*\d{16}\s*')
NAME_REGEX = re.compile(r"^[A-Za-z\s'-]+$")


def is_phone(text):
    return bool(PHONE_REGEX.search(text))

def is_ssn(text):
    return bool(SSN_REGEX.search(text))

def is_dob(text):
    return bool(DOB_REGEX.search(text))

def is_ip(text):
    return bool(IP_REGEX.search(text))

def is_name(text):
    return bool(NAME_REGEX.match(text))