import pytest
import logging
from common.constants import SearchStrings

logger = logging.getLogger()


class TestSearch:
    """
    1. Ввести строку в поле поиска
    2. Нажать на кнопку с лупой
    3. Проверить заголовки найденных элементов на вхождение заданной строки
    """

    @pytest.mark.parametrize(
        "search_str, expected_result",
        [
            pytest.param(
                SearchStrings.PART_OF_WORD, True, id='1."Search by part of word"'
            ),
            pytest.param(SearchStrings.ONE_WORD, True, id='2."Search by full word"'),
            pytest.param(SearchStrings.TWO_WORDS, True, id='3."Search by two words"'),
        ],
    )
    def test_search_positive(self, app, search_str, expected_result):
        app.open_main_page()
        logger.info(f'Input string "{search_str}" into search field')
        app.search.run_search(search_str)
        result = app.search.check_found_item(search_str)
        assert result == expected_result

    @pytest.mark.parametrize(
        "search_str, expected_result",
        [
            pytest.param(
                SearchStrings.ONE_WORD_NEGATIVE, False, id='1."Search by one word"'
            ),
            pytest.param(
                SearchStrings.TWO_WORDS_NEGATIVE, False, id='2."Search by two words"'
            ),
        ],
    )
    def test_search_negative(self, app, search_str, expected_result):
        app.open_main_page()
        app.search.run_search(search_str)
        result = app.search.check_found_item(search_str)
        assert result == expected_result