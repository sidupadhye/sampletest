import pytest

@pytest.mark.smoke
def test_sample_four():
    print("Inside sample four")

#@pytest.mark.sanity
@pytest.mark.xfail
def test_Sample_five():
    print("Inside Sample five")

@pytest.mark.regression
def test_Sample_six():
    print("Inside Sample six")
