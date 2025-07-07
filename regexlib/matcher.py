from . import patterns

def is_uscan_phone(text):
    return bool(patterns.USCAN_PHONE_REGEX.pattern.search(text))

def is_inter_phone(text):
		return bool(patterns.INTER_PHONE_REGEX.pattern.search(text))

def is_ssn(text):
    return bool(patterns.SSN_REGEX.pattern.search(text))

def is_dob(text):
    return bool(patterns.DOB_REGEX.pattern.search(text))

def is_ip(text):
    return bool(patterns.IP_REGEX.pattern.search(text))

def is_driver_license(text):
		return bool(patterns.DL_REGEX.pattern.search(text))

def is_email(text):
    return bool(patterns.EMAIL_REGEX.pattern.search(text))
