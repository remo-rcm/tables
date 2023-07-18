import cordex as cx
import pandas as pd
import pytest

url = "./domains/domains.csv"


@pytest.fixture
def domain_table():
    return pd.read_csv(url).set_index("domain_id")


def test_table(domain_table):
    df = domain_table
    for domain_id in df.index:
        print(domain_id)
        assert cx.cordex_domain(domain_id, tables=df)
