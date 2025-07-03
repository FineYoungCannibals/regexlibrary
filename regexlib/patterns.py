import re

# Precompiled patterns
USCAN_PHONE_REGEX = re.compile(r'(\+1[-.\s]?)?(\(?\d{3}\)?[-.\s]?){1}\d{3}[-.\s]?\d{4}')
INTER_PHONE_REGEX = re.compile(r'\+[0-9\s\-().]{7,20}')
SSN_REGEX = re.compile(r'\d{3}-\d{2}-\d{4}|\d{3}\s*\d{3}\s*\d{3}')
DOB_REGEX = re.compile(r'\d{1,2}[/-]\d{1,2}[/-]\d{2,4}|\d{2,4}[/-]\d{1,2}[/-]\d{1,2}')
IP_REGEX = re.compile(r'\d{1,3}(\.\d{1,3}){3}')
CC_REGEX = re.compile(r'\s*\d{16}\s*')
DL_REGEX = re.compile(r'[A-Z]{0,3}[0-9]+', re.IGNORECASE)


def is_uscan_phone(text):
    return bool(USCAN_PHONE_REGEX.search(text))

def is_inter_phone(text):
		return bool(INTER_PHONE_REGEX.search(text))

def is_ssn(text):
    return bool(SSN_REGEX.search(text))

def is_dob(text):
    return bool(DOB_REGEX.search(text))

def is_ip(text):
    return bool(IP_REGEX.search(text))

def is_driver_license(text):
		return bool(DL_REGEX.search(text))
