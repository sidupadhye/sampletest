import pytest

@pytest.mark.smoke
def test_sample_one():
    print("Inside the test Sample one")

@pytest.mark.sanity
def test_sample_two():
    print("Inside the test Sample two")

@pytest.mark.regression
def test_sample_three():
    print("Inside the test Sample three")

@pytest.mark.regression
def test_sample_four():
    print("Inside the test sample four ")

@pytest.mark.sanity
def test_sample_five():
    print("Inside the test sample five")

@pytest.mark.smoke
def test_sample_six():
    print("Inside  the test sample six")