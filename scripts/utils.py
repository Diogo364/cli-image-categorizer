import os
from string import ascii_lowercase, digits

def create_directory(dirname):
    os.mkdir(dirname)
    return 1

def move_to_directory(filename1, filename2):
    os.rename(filename1, filename2)
    return 1

def is_directory(directory):
    return os.path.isdir(directory)

def parse_cv2_pressed_key_to_char(pressed_key):
    return chr(pressed_key & 255)

def get_valid_keys_for_classes(reserved_letters=['q', 'h']):
    valid_keys = ascii_lowercase + digits
    valid_keys_list = list(valid_keys)
    for key in reserved_letters:
        valid_keys_list.remove(key)
    return valid_keys_list