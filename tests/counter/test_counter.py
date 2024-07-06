from src.pre_built.counter import count_ocurrences

import pytest


@pytest.fixture
def find_test_file():
    test_file = "data/jobs.csv"
    return test_file


def test_counter(find_test_file):
    """Testa a contagem de ocorrências de uma palavra existente."""
    word = "secure"
    count = count_ocurrences(find_test_file, word)
    assert count == 245
