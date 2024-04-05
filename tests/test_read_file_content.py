import pytest
from main import read_file_content   

@pytest.mark.parametrize("file_name, expected_lines", [
    ('test_file.txt', ['Це тестовий файл.\n', 'Це другий рядок.\n']),
])
def test_read_file_content(create_test_file, file_name, expected_lines):
    assert read_file_content(file_name) == expected_lines

@pytest.mark.parametrize("invalid_input", [
    (123),  
    (True),  
    (None),  
    ([])     
])
def test_read_file_content_invalid_input(invalid_input):
    with pytest.raises(TypeError):
        read_file_content(invalid_input)
