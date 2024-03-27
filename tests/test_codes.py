import pandas as pd
import pytest

url = "./code-list/table.csv"


@pytest.fixture
def code_table():
    return pd.read_csv(url).set_index("code")


def test_unique_codes():
    df = pd.read_csv(url)
    assert df.code.is_unique
