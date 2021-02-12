#--Common Pattern--#
import re

#define some pattern
pattern = re.compile(r'\b\d{3} \d{3}-\d{4}\b') #gotta use the r so that we can use typical backslashes

#search whatever with the regex
res = pattern.search('call me at 801 845-3332')

#function creation example
def extract_phone(entry):
    phone_regex = re.compile(r'\b\d{3} \d{3}-\d{4}\b')
    return phone_regex.findall(entry)

def is_valid_phone(entry):
    phone_regex = re.compile(r'^\d{3} \d{3}-\d{4}$')
    match = phone_regex.search(entry)
    if match:
        return True
    return False

def parse_date(entry):
    date_regex = re.compile(r"(\d\d)(/|\.|,)(\d\d)(/|\.|,)(\d\d\d\d)")
    match = date_regex.fullmatch(entry)
    if match:
        return print({"d":match.group(1), "m":match.group(3), "y":match.group(5)})

parse_date("12.30.1200")
