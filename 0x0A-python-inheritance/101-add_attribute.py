#!/usr/bin/python3
"""
    101-dd_attribute()
"""

def add_attribute(obj, attr_name, attr_value):
    """
    Add a new attribute to an object if it's possible.

    Args:
        obj: The object to add the attribute to.
        attr_name: The name of the attribute.
        attr_value: The value of the attribute.

    Raises:
        TypeError: If the object cannot have a new attribute.

    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr_name, attr_value)
