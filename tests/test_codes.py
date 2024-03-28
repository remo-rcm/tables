import pandas as pd
import pytest

url = "./code-list/table.csv"


@pytest.fixture
def code_table():
    return pd.read_csv(url).set_index("code")


def test_unique_codes():
    df = pd.read_csv(url)
    # code and variable names should be unique (execpt PHI, RLA)
    assert df.code.is_unique
    assert (
        df.variable.dropna().drop(df[df.variable.isin(("PHI", "RLA"))].index).is_unique
    )
