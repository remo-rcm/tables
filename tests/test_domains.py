import cordex as cx
import pandas as pd
import pyremo as pr
import pytest

url = "./domains/domains.csv"


@pytest.fixture
def domain_table():
    return pd.read_csv(url).set_index("domain_id")


def test_table(domain_table):
    df = domain_table
    for domain_id in df.index:
        assert cx.cordex_domain(domain_id, tables=df)


def test_magic_numbers(domain_table):
    # test if nlon and nlat are magic number
    magic_numbers = pr.magic_numbers()
    print(f"magic_numbers: {magic_numbers}")
    df = domain_table
    for domain_id, row in df.iterrows():
        assert row.nlon in magic_numbers
        assert row.nlat in magic_numbers
