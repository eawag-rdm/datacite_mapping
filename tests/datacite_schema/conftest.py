import pytest
import pathlib


@pytest.fixture()
def data_folder():
    return pathlib.Path(__file__).parent / ("data")



