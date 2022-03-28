import pytest


@pytest.mark.regress
def test_regress_one():
    assert 2 + 2 == 1, f"Error"


@pytest.mark.smoke
def test_smoke_one():
    assert 120 + 10 == 20, f'NO'


@pytest.mark.regress
def test_regress_two():
    assert 10 + 102 == 112, f'OK'


@pytest.mark.regress
def test_regress_3():
    assert 10 + 10 == 220, f'Error'


@pytest.mark.skip
def test_skip():
    assert 10 + 10 == 30, f'Skip'
