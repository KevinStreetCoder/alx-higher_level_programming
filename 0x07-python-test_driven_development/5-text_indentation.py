#!/usr/bin/python3

"""
Module: 5-text_indentation
Contains:
    Function: text_indentation(text)
"""

def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
        text (str): The input text.

    Raises:
        TypeError: If text is not a string.

    Returns:
        None
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    new_text = ""
    skip_space = True

    for char in text:
        if skip_space and char == ' ':
            continue

        new_text += char
        skip_space = False

        if char in ['.', '?', ':']:
            new_text += '\n\n'
            skip_space = True

    print(new_text.strip())
