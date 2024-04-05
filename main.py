def read_file_content(file_name: str) -> list:
    """
    Reads the contents of a file and returns it as a list of strings.
    :param: the name of the file to read
    :return: the list of string
    """
    if not isinstance(file_name, str):
        raise TypeError("invalid_input")
    with open(file_name, 'r', encoding='utf-8') as file:
        return file.readlines()

def filter_lines_by_keyword(lines: list[str], keyword: str) -> list[str]:
    """
    Selects strings that contain a specific keyword and returns them.
    
    :param lines: A list of strings among which to search for the keyword.
    :param keyword: The keyword to search for within the list of strings.
    :return: A list of strings that contain the keyword.
    """
    if not isinstance(lines, list) or not all(isinstance(line, str) for line in lines):
        raise TypeError("lines must be a list of lines.")
    if not isinstance(keyword, str):
        raise TypeError("keyword must be a string type.")
    keyword_lower = keyword.lower()
    return [line for line in lines if keyword_lower in line.lower()]

def write_filtered_content(filtered_lines: list[str], file_name: str) -> None:
    """
    Writes the given list of strings to a file.

    :param filtered_lines: A list of strings to write to the file.
    :param file_name: The name of the file to which the strings are to be written.
    """
    if not isinstance(filtered_lines, list) or not all(isinstance(line, str) for line in filtered_lines):
        raise TypeError("filtered_lines must be a list of lines.")
    if not isinstance(file_name, str):
        raise TypeError("file_name must be a string type.")
    
    with open(file_name, 'w', encoding='utf-8') as file:
        file.writelines(filtered_lines)