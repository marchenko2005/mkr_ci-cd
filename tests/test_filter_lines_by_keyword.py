import pytest 
from main import filter_lines_by_keyword

@pytest.mark.parametrize("lines, keyword, expected_result", [
    (['One line', 'Two line', 'Red line', 'Blue line'], 'line', ['One line', 'Two line', 'Red line', 'Blue line']),
    (['case sensitive', 'Case Sensitive', 'CASE'], 'case', ['case sensitive', 'Case Sensitive', 'CASE']),
    (['Python programming', 'is fun', 'and useful'], 'python', ['Python programming']),
    ([], 'empty', []),  
    (['No match here'], 'python', [])  
])
def test_filter_lines_by_keyword(lines, keyword, expected_result):
    assert filter_lines_by_keyword(lines, keyword) == expected_result

@pytest.mark.parametrize("invalid_lines, keyword", [
    (123, 'test'),  
    ([], 123),  
    (True, 'test'),  
    (['valid', 'list'], None)  
])
def test_filter_lines_by_keyword_invalid_input(invalid_lines, keyword):
    with pytest.raises(TypeError):
        filter_lines_by_keyword(invalid_lines, keyword)

@pytest.mark.parametrize("lines, keyword", [
    (['Case Insensitive', 'case Insensitive', 'CASE INSENSITIVE'], 'case'),
    (['mIxEd CaSe', 'Mixed CASE', 'mixED Case'], 'mixed')
])
def test_filter_lines_by_keyword_case_insensitive(lines, keyword):
    result = filter_lines_by_keyword(lines, keyword)
    assert len(result) == len(lines)  
    for line in result:
        assert keyword.lower() in line.lower()