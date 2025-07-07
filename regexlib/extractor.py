from . import patterns

def extract_uscan_phone(text):
    return patterns.USCAN_PHONE_REGEX.pattern.findall(text)

def extract_inter_phone(text):
		return patterns.INTER_PHONE_REGEX.pattern.findall(text)

def extract_ssn(text):
    return patterns.SSN_REGEX.pattern.findall(text)

def extract_dob(text):
    return patterns.DOB_REGEX.pattern.findall(text)

def extract_ip(text):
    return patterns.IP_REGEX.pattern.findall(text)

def extract_driver_license(text):
		return patterns.DL_REGEX.pattern.findall(text)

def extract_email(text):
    return patterns.EMAIL_REGEX.pattern.findall(text)
