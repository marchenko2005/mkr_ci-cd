import pytest
from main import write_filtered_content 


def test_write_filtered_content(temp_file):
    lines_to_write = ["Перший рядок\n", "Другий рядок\n", "Третій рядок\n"]
    file_name = str(temp_file)
    
    write_filtered_content(lines_to_write, file_name)

    assert temp_file.exists(), "The file was not created"
    with open(file_name, 'r', encoding='utf-8') as file:
        content = file.readlines()
    assert content == lines_to_write, "The contents of the file are not as expected"

@pytest.mark.parametrize("filtered_lines, file_name", [
    (123, 'valid_file_name.txt'), 
    (['valid', 'list'], 123), 
])
def test_write_filtered_content_invalid_input(filtered_lines, file_name, temp_file):
    with pytest.raises(TypeError):
        write_filtered_content(filtered_lines, file_name)
