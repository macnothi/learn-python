#!/usr/bin/env python3

def convert_to_snake_case(pascal_or_camel_cased_string):
    snake_cased_char_list = []
    for char in pascal_or_camel_cased_string:
        if char.isupper():
            converted_character = '_' + str(char).lower()
            print(converted_character)

    pascal_or_camel_cased_string = "JensNothnagelsCamelString"    
    for char in pascal_or_camel_cased_string:
        print(char)
        if char.isupper():
            converted_character = '_' + str(char).lower()
            print(converted_character)
        