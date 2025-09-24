#!/usr/bin/python3
"""
XML serialization and deserialization module
"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serialize a Python dictionary to XML format

    Args:
        dictionary (dict): Python dictionary to serialize
        filename (str): The filename to save the XML data

    Returns:
        bool: True if successful, False otherwise
    """
    try:
        # Create root element
        root = ET.Element("data")

        # Iterate through dictionary items and create XML elements
        for key, value in dictionary.items():
            # Create child element with key as tag name
            child = ET.SubElement(root, key)
            # Convert value to string and set as text content
            child.text = str(value)

        # Create ElementTree and write to file
        tree = ET.ElementTree(root)
        tree.write(filename, encoding='utf-8', xml_declaration=True)

        print(f"Dictionary serialized to {filename}")
        return True

    except Exception as e:
        print(f"Serialization error: {e}")
        return False


def deserialize_from_xml(filename):
    """
    Deserialize XML data to Python dictionary

    Args:
        filename (str): The filename to read the XML data from

    Returns:
        dict: Deserialized Python dictionary or None if error
    """
    try:
        # Parse the XML file
        tree = ET.parse(filename)
        root = tree.getroot()

        # Reconstruct dictionary from XML elements
        result_dict = {}

        for child in root:
            result_dict[child.tag] = child.text

        print(f"Data deserialized from {filename}")
        return result_dict

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None
    except ET.ParseError:
        print(f"Error: Invalid XML format in '{filename}'.")
        return None
    except Exception as e:
        print(f"Deserialization error: {e}")
        return None
