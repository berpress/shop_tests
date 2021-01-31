import pytest


class TestSearch:
    """
    1. Ввести строку в поле поиска
    2. Нажать на кнопку с лупой
    3. Проанализировать результаты
    4. Проверить заголовки найденных элементов на вхождение заданной строки
    """

    @pytest.mark.parametrize(
        "search_str, expected_result",
        [
            pytest.param("Prin", True, id='1."Search by part of word"'),
            pytest.param("dress", True, id='2."Search by full word"'),
            pytest.param("siurhfsuew", False, id='2."Negative case"'),
        ],
    )
    def test_search(self, app, search_str, expected_result):
        app.open_main_page()
        app.search.run_search(search_str)
        result = app.search.check_found_item(search_str)
        assert result == expected_result
