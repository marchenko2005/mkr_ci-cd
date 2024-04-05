import pytest 
import os

@pytest.fixture
def create_test_file():
    file_name = "test_file.txt"
    with open(file_name, 'w', encoding='utf-8') as file:
        file.writelines(['Це тестовий файл.\n', 'Це другий рядок.\n'])
    yield file_name  
    os.remove(file_name) 


@pytest.fixture
def temp_file(tmp_path):
    file = tmp_path / "test_file.txt"
    yield file
    if file.exists():
        file.unlink()