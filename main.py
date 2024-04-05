def read_file_content(filename):
    """Зчитує вміст файлу та повертає його як список рядків."""
    with open(filename, 'r', encoding='utf-8') as file:
        return file.readlines()

def filter_lines_by_keyword(lines, keyword):
    """Відбирає рядки, які містять ключове слово, та повертає їх."""
    return [line for line in lines if keyword in line]

def write_to_file(filename, lines):
    """Записує дані у файл."""
    with open(filename, 'w', encoding='utf-8') as file:
        file.writelines(lines)

# Використання функцій
if __name__ == "__main__":
    input_filename = 'text.txt'  # Назва вхідного файлу
    output_filename = 'filtered.txt'  # Назва вихідного файлу
    keyword = 'УПА'  # Ключове слово для пошуку

    # Зчитування вмісту файлу
    content = read_file_content(input_filename)
    
    # Фільтрація рядків за ключовим словом
    filtered_lines = filter_lines_by_keyword(content, keyword)
    
    # Запис відфільтрованих рядків у новий файл
    write_to_file(output_filename, filtered_lines)

    print(f"Файл '{output_filename}' було успішно створено з відфільтрованим вмістом.")
