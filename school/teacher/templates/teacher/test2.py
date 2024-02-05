import re

def remove_symbols_between_alphanumeric(input_string):
    pattern = r'(?<=[A-Za-z0-9])[^A-Za-z0-9]+(?=[A-Za-z0-9])'
    decoded_string = re.sub(pattern, ' ', input_string)
    return decoded_string

input_string = "This$#is% Matrix#  %!"
decoded_script = remove_symbols_between_alphanumeric(input_string)
print(decoded_script)