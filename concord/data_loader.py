# data_loader.py

import json


def load_element_mock_messages():
    """
    Load the element_mock_messages dataset from a JSON file for topic modeling.
    Assumes JSON file format as [{"message": "text1"}, {"message": "text2"}, ...]

    Returns:
    list: List of document strings for topic analysis.
    """
    filepath = "/home/saj/PycharmProjects/Concord/concord/element_mock_messages.json"  # Absolute path

    with open(filepath, "r", encoding="utf-8") as file:
        data = json.load(file)

    # Extract 'message' field from each entry in the JSON list
    documents = [entry['message'] for entry in data if 'message' in entry]

    return documents
