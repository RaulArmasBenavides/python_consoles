import re

# Define the regular expressions
regex_integer_in_range = r"^[1-9][0-9]{5}$"  # Matches integers in the range 100000 to 999999
regex_alternating_repetitive_digit_pair = r"(?=(\d)\d\1)"  # Matches alternating repetitive digit pairs

# Read the postal code
P = input()

# Check validity of the postal code
is_valid = (
    bool(re.match(regex_integer_in_range, P))  # Check range
    and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2  # Check alternating pairs
)

print(is_valid)