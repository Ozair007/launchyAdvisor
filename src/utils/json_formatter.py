def json_formatter(text):
    """
    Removes leading ```json and trailing ``` from a JSON string.

    Args:
            text (str): The JSON string to format.

    Returns:
            str: A formatted JSON string.
    """
    if text.startswith("```json"):
        text = text[len("```json"):].strip()
    if text.endswith("```"):
        text = text[:-len("```")].strip()
    return text
